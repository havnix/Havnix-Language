# havnix.py - Havnix Language Interpreter & Package Manager
# لغة هافنيكس - لغة برمجة عربية باللهجة السودانية

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.interpreter import HavnixInterpreter

VERSION = "2.0.0"


def show_help():
    print(f"هافنيكس {VERSION} | Havnix Programming Language")
    print("=" * 50)
    print()
    print("الاستخدام:")
    print("  havnix <ملف.havnix>            → تشغيل ملف هافنيكس")
    print("  havnix install <اسم_المكتبة>   → تثبيت مكتبة")
    print("  havnix uninstall <اسم_المكتبة> → إزالة مكتبة")
    print("  havnix update <اسم_المكتبة>    → تحديث مكتبة")
    print("  havnix list                     → عرض المكتبات المثبتة")
    print("  havnix search <كلمة>            → بحث عن مكتبات")
    print("  havnix info <اسم_المكتبة>      → معلومات عن مكتبة")
    print("  havnix init                     → إنشاء مشروع جديد")
    print()
    print("الأوامر الأساسية:")
    print('  قول ليهو("نص")           → طباعة نص')
    print('  $اسم = "قيمة";           → تعريف متغير')
    print('  لو (شرط) { }             → جملة شرطية')
    print('  طالما (شرط) { }          → حلقة تكرارية')
    print('  لكل $عنصر في $قائمة { }  → تكرار على قائمة')
    print('  دالة اسم(معاملات) { }    → تعريف دالة')
    print('  جيب لي اسم(قيم);         → استدعاء دالة')
    print('  استورد "مكتبة";          → استيراد مكتبة')
    print()
    print("للمزيد من المعلومات اقرأ ملف GUIDE.md")


def main():
    if len(sys.argv) < 2:
        print(f"هافنيكس {VERSION} | Havnix Programming Language")
        print("لغة برمجة عربية باللهجة السودانية")
        print()
        print("الاستخدام: havnix <ملف.havnix>")
        print("           havnix install <مكتبة>")
        print("           havnix --help")
        sys.exit(0)

    arg = sys.argv[1]

    if arg in ('--نسخة', '--version', '-v'):
        print(f"Havnix {VERSION}")
        sys.exit(0)

    if arg in ('--مساعدة', '--help', '-h'):
        show_help()
        sys.exit(0)

    # Package management commands
    if arg in ('install', 'تثبيت'):
        from core.package_manager import PackageManager
        pm = PackageManager()
        if len(sys.argv) < 3:
            print("خطأ: حدد اسم المكتبة. مثال: havnix install التقويم_الهجري")
            sys.exit(1)
        pkg_name = sys.argv[2]
        pm.install(pkg_name)
        sys.exit(0)

    if arg in ('uninstall', 'إزالة'):
        from core.package_manager import PackageManager
        pm = PackageManager()
        if len(sys.argv) < 3:
            print("خطأ: حدد اسم المكتبة. مثال: havnix uninstall التقويم_الهجري")
            sys.exit(1)
        pkg_name = sys.argv[2]
        pm.uninstall(pkg_name)
        sys.exit(0)

    if arg in ('update', 'تحديث'):
        from core.package_manager import PackageManager
        pm = PackageManager()
        if len(sys.argv) < 3:
            print("خطأ: حدد اسم المكتبة. مثال: havnix update التقويم_الهجري")
            sys.exit(1)
        pkg_name = sys.argv[2]
        pm.update(pkg_name)
        sys.exit(0)

    if arg in ('list', 'قائمة'):
        from core.package_manager import PackageManager
        pm = PackageManager()
        pm.list_installed()
        sys.exit(0)

    if arg in ('search', 'بحث'):
        from core.package_manager import PackageManager
        pm = PackageManager()
        query = sys.argv[2] if len(sys.argv) > 2 else ""
        pm.search(query)
        sys.exit(0)

    if arg in ('info', 'معلومات'):
        from core.package_manager import PackageManager
        pm = PackageManager()
        if len(sys.argv) < 3:
            print("خطأ: حدد اسم المكتبة. مثال: havnix info التقويم_الهجري")
            sys.exit(1)
        pm.info(sys.argv[2])
        sys.exit(0)

    if arg in ('init', 'مشروع'):
        from core.package_manager import PackageManager
        pm = PackageManager()
        pm.init_project()
        sys.exit(0)

    # Run a .havnix file
    if not os.path.isfile(arg):
        print(f"خطأ: الملف '{arg}' غير موجود")
        sys.exit(1)

    interpreter = HavnixInterpreter()
    interpreter.run(arg)


if __name__ == "__main__":
    main()
