"""
Havnix Package Manager - مدير مكتبات هافنيكس
Handles install, uninstall, update, search, and project init
"""

import json
import os
import shutil
import sys


class PackageManager:
    def __init__(self):
        # Havnix installation directory (where havnix.py lives)
        self.havnix_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Official packages directory (in the Havnix installation)
        self.packages_dir = os.path.join(self.havnix_root, 'packages')
        # Registry file
        self.registry_file = os.path.join(self.packages_dir, 'registry.json')
        # Project directory (current working directory)
        self.project_dir = os.getcwd()
        # Local libraries directory
        self.lib_dir = os.path.join(self.project_dir, 'havnix_libraries')
        # Project libraries.json
        self.libs_json = os.path.join(self.project_dir, 'libraries.json')

    def _load_registry(self):
        """Load the package registry"""
        if not os.path.exists(self.registry_file):
            print("خطأ: ملف السجل غير موجود. تأكد من تثبيت هافنيكس بشكل صحيح.")
            return None
        with open(self.registry_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _load_libs_json(self):
        """Load the project's libraries.json"""
        if os.path.exists(self.libs_json):
            with open(self.libs_json, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {"name": os.path.basename(self.project_dir), "version": "1.0.0", "libraries": {}}

    def _save_libs_json(self, data):
        """Save the project's libraries.json"""
        with open(self.libs_json, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def _find_package(self, name):
        """Find a package by name (with or without version)"""
        # Handle name@version format
        version = None
        if '@' in name:
            name, version = name.rsplit('@', 1)

        registry = self._load_registry()
        if not registry:
            return None, None

        for pkg in registry.get('packages', []):
            if pkg['name'] == name:
                if version and pkg['version'] != version:
                    print(f"تحذير: الإصدار {version} غير متوفر. يتم تثبيت {pkg['version']}")
                return pkg, name

        return None, name

    def install(self, pkg_input):
        """Install a package"""
        # Parse name@version
        name = pkg_input
        version = None
        if '@' in pkg_input:
            name, version = pkg_input.rsplit('@', 1)

        pkg, clean_name = self._find_package(pkg_input)

        if not pkg:
            print(f"خطأ: المكتبة '{clean_name}' غير موجودة في السجل.")
            print()
            print("المكتبات المتوفرة:")
            self.search("")
            return False

        # Create havnix_libraries directory
        os.makedirs(self.lib_dir, exist_ok=True)

        # Check if already installed
        pkg_dest = os.path.join(self.lib_dir, pkg['name'])
        if os.path.exists(pkg_dest):
            print(f"المكتبة '{pkg['name']}' مثبتة بالفعل (الإصدار {pkg['version']})")
            print(f"استخدم 'havnix update {pkg['name']}' للتحديث")
            return False

        # Copy package files
        pkg_src = os.path.join(self.packages_dir, pkg['name'])
        if not os.path.exists(pkg_src):
            print(f"خطأ: ملفات المكتبة '{pkg['name']}' غير موجودة.")
            return False

        shutil.copytree(pkg_src, pkg_dest)
        print(f"[+] تم تثبيت '{pkg['name']}' الإصدار {pkg['version']}")

        # Update libraries.json
        libs = self._load_libs_json()
        libs['libraries'][pkg['name']] = pkg['version']
        self._save_libs_json(libs)
        print(f"[+] تم تحديث libraries.json")

        # Show usage
        print()
        print(f"للاستخدام، أضف في بداية ملفك:")
        main_file = pkg.get('main', pkg['name'] + '.havnix')
        print(f'  استورد "havnix_libraries/{pkg["name"]}/{main_file}";')
        return True

    def uninstall(self, name):
        """Uninstall a package"""
        pkg_dest = os.path.join(self.lib_dir, name)
        if not os.path.exists(pkg_dest):
            print(f"خطأ: المكتبة '{name}' غير مثبتة.")
            return False

        shutil.rmtree(pkg_dest)
        print(f"[-] تم إزالة '{name}'")

        # Update libraries.json
        libs = self._load_libs_json()
        if name in libs.get('libraries', {}):
            del libs['libraries'][name]
            self._save_libs_json(libs)
            print(f"[-] تم تحديث libraries.json")

        return True

    def update(self, name):
        """Update a package"""
        pkg_dest = os.path.join(self.lib_dir, name)
        if not os.path.exists(pkg_dest):
            print(f"خطأ: المكتبة '{name}' غير مثبتة. استخدم 'havnix install {name}' أولاً")
            return False

        pkg, clean_name = self._find_package(name)
        if not pkg:
            print(f"خطأ: المكتبة '{name}' غير موجودة في السجل.")
            return False

        # Check current version
        local_pkg_json = os.path.join(pkg_dest, 'package.json')
        current_version = "0.0.0"
        if os.path.exists(local_pkg_json):
            with open(local_pkg_json, 'r', encoding='utf-8') as f:
                local_data = json.load(f)
                current_version = local_data.get('version', '0.0.0')

        if current_version == pkg['version']:
            print(f"المكتبة '{name}' محدثة بالفعل (الإصدار {pkg['version']})")
            return False

        # Remove old and install new
        shutil.rmtree(pkg_dest)
        pkg_src = os.path.join(self.packages_dir, pkg['name'])
        shutil.copytree(pkg_src, pkg_dest)
        print(f"[+] تم تحديث '{name}' من {current_version} إلى {pkg['version']}")

        # Update libraries.json
        libs = self._load_libs_json()
        libs['libraries'][name] = pkg['version']
        self._save_libs_json(libs)

        return True

    def list_installed(self):
        """List installed packages"""
        libs = self._load_libs_json()
        installed = libs.get('libraries', {})

        if not installed:
            print("لا توجد مكتبات مثبتة.")
            print()
            print("لتثبيت مكتبة: havnix install <اسم_المكتبة>")
            print("للبحث عن مكتبات: havnix search")
            return

        print(f"المكتبات المثبتة ({len(installed)}):")
        print("-" * 40)
        for name, version in installed.items():
            # Check if files exist
            exists = "✓" if os.path.exists(os.path.join(self.lib_dir, name)) else "✗"
            print(f"  {exists} {name} @ {version}")
        print("-" * 40)

    def search(self, query=""):
        """Search for packages"""
        registry = self._load_registry()
        if not registry:
            return

        packages = registry.get('packages', [])
        results = []

        for pkg in packages:
            if not query or query in pkg['name'] or query in pkg.get('description', '') or any(query in kw for kw in pkg.get('keywords', [])):
                results.append(pkg)

        if not results:
            print(f"لا توجد مكتبات مطابقة لـ '{query}'")
            return

        print(f"المكتبات المتوفرة ({len(results)}):")
        print("-" * 60)
        for pkg in results:
            # Check if installed
            installed = ""
            if os.path.exists(os.path.join(self.lib_dir, pkg['name'])):
                installed = " [مثبتة]"
            print(f"  {pkg['name']} @ {pkg['version']}{installed}")
            print(f"    {pkg['description']}")
            print()

    def info(self, name):
        """Show package info"""
        pkg, clean_name = self._find_package(name)
        if not pkg:
            print(f"خطأ: المكتبة '{clean_name}' غير موجودة.")
            return

        print(f"{'=' * 50}")
        print(f"  اسم المكتبة: {pkg['name']}")
        print(f"  الإصدار: {pkg['version']}")
        print(f"  الوصف: {pkg['description']}")
        print(f"  المطور: {pkg.get('author', 'غير معروف')}")
        print(f"  الرخصة: {pkg.get('license', 'غير محددة')}")
        print(f"  الملف الرئيسي: {pkg.get('main', pkg['name'] + '.havnix')}")
        keywords = pkg.get('keywords', [])
        if keywords:
            print(f"  الكلمات المفتاحية: {', '.join(keywords)}")
        print(f"{'=' * 50}")

        # Check if installed
        if os.path.exists(os.path.join(self.lib_dir, pkg['name'])):
            print("  الحالة: مثبتة")
        else:
            print("  الحالة: غير مثبتة")
            print(f"  للتثبيت: havnix install {pkg['name']}")

        print()
        print("  للاستخدام:")
        main_file = pkg.get('main', pkg['name'] + '.havnix')
        print(f'    استورد "havnix_libraries/{pkg["name"]}/{main_file}";')

    def init_project(self):
        """Initialize a new Havnix project"""
        if os.path.exists(self.libs_json):
            print("المشروع موجود بالفعل (libraries.json موجود)")
            return

        project_name = os.path.basename(self.project_dir)
        data = {
            "name": project_name,
            "version": "1.0.0",
            "description": "",
            "author": "",
            "main": "main.havnix",
            "libraries": {}
        }
        self._save_libs_json(data)
        print(f"[+] تم إنشاء مشروع '{project_name}'")
        print(f"[+] تم إنشاء libraries.json")

        # Create main.havnix if it doesn't exist
        main_file = os.path.join(self.project_dir, 'main.havnix')
        if not os.path.exists(main_file):
            with open(main_file, 'w', encoding='utf-8') as f:
                f.write('// مشروع هافنيكس جديد\n')
                f.write(f'// {project_name}\n')
                f.write('\n')
                f.write('قول ليهو("مرحبا بالعالم!");\n')
            print(f"[+] تم إنشاء main.havnix")

        # Create havnix_libraries directory
        os.makedirs(self.lib_dir, exist_ok=True)
        print(f"[+] تم إنشاء مجلد havnix_libraries/")
        print()
        print("الخطوات التالية:")
        print(f"  1. عدّل main.havnix واكتب كودك")
        print(f"  2. ثبّت مكتبات: havnix install <اسم_المكتبة>")
        print(f"  3. شغّل البرنامج: havnix main.havnix")
