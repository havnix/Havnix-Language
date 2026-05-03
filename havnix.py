# havnix.py - Havnix Language Interpreter
# لغة هافنيكس - لغة برمجة عربية باللهجة السودانية

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.interpreter import HavnixInterpreter

VERSION = "2.0.0"


def main():
    if len(sys.argv) < 2:
        print(f"هافنيكس {VERSION} | Havnix Programming Language")
        print("لغة برمجة عربية باللهجة السودانية")
        print()
        print("الاستخدام: python havnix.py <ملف.havnix>")
        print()
        print("الخيارات:")
        print("  --نسخة, --version    عرض رقم الإصدار")
        print("  --مساعدة, --help     عرض المساعدة")
        sys.exit(0)

    arg = sys.argv[1]

    if arg in ('--نسخة', '--version', '-v'):
        print(f"Havnix {VERSION}")
        sys.exit(0)

    if arg in ('--مساعدة', '--help', '-h'):
        print(f"هافنيكس {VERSION} | Havnix Programming Language")
        print("=" * 50)
        print()
        print("الاستخدام:")
        print("  python havnix.py <ملف.havnix>")
        print()
        print("مثال:")
        print("  python havnix.py main.havnix")
        print()
        print("الأوامر الأساسية:")
        print('  قول ليهو("نص")           → طباعة نص')
        print('  $اسم = "قيمة";           → تعريف متغير')
        print('  لو (شرط) { }             → جملة شرطية')
        print('  طالما (شرط) { }          → حلقة تكرارية')
        print('  لكل $عنصر في $قائمة { }  → تكرار على قائمة')
        print('  دالة اسم(معاملات) { }    → تعريف دالة')
        print('  جيب لي اسم(قيم);         → استدعاء دالة')
        print()
        print("للمزيد من المعلومات اقرأ ملف GUIDE.md")
        sys.exit(0)

    if not os.path.isfile(arg):
        print(f"خطأ: الملف '{arg}' غير موجود")
        sys.exit(1)

    interpreter = HavnixInterpreter()
    interpreter.run(arg)


if __name__ == "__main__":
    main()
