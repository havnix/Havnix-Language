# كيفية تشغيل لغة هافنيكس 🇸🇩

## المتطلبات
- **Python 3.8+** ([تحميل من هنا](https://www.python.org/downloads/))

## التثبيت

```bash
# 1. حمل المشروع
git clone https://github.com/Snixrs/Havnix-Language.git
cd Havnix-Language

# 2. ثبت المكتبات (اختياري - للميزات المتقدمة)
pip install -r requirements.txt
```

## طرق التشغيل

### 1. تشغيل ملف .havnix مباشرة

```bash
python havnix.py examples/hello.havnix
```

### 2. تشغيل IDE بيئة التطوير المتكاملة

```bash
# على Linux/Mac
python3 ide.py

# على Windows
python ide.py
# أو انقر مرتين على run_ide.bat
```

سيفتح المتصفح تلقائياً على `http://localhost:8585`

### 3. بناء ملف EXE (Windows)

```bash
python build_exe.py
# الملف التنفيذي: dist/HavnixIDE.exe
```

## ميزات IDE

| الميزة | الوصف |
|--------|-------|
| **تلوين الكود** | تلوين تلقائي للكلمات المفتاحية والمتغيرات والنصوص |
| **RTL** | دعم الكتابة من اليمين لليسار |
| **مستكشف الملفات** | تصفح وفتح الملفات من الشريط الجانبي |
| **طرفية تفاعلية** | تشغيل أوامر Bash و Git مباشرة |
| **تشغيل بـ F5** | تشغيل الكود بضغطة زر |
| **حفظ بـ Ctrl+S** | حفظ سريع للملفات |

## اختصارات لوحة المفاتيح

| الاختصار | الوظيفة |
|----------|---------|
| `F5` | تشغيل البرنامج |
| `Ctrl + S` | حفظ الملف |
| `Ctrl + N` | ملف جديد |
| `Ctrl + O` | فتح ملف |
| `Tab` | إضافة مسافة بادئة |

## أمثلة سريعة

### طباعة نص
```
قول ليهو("مرحبا يا عالم!");
```

### متغيرات
```
$الاسم = "أحمد";
$العمر = 25;
قول ليهو("اسمي $الاسم وعمري $العمر");
```

### شروط
```
لو ($العمر >= 18) {
    قول ليهو("كبير");
} غير كدا {
    قول ليهو("صغير");
}
```

### حلقات
```
$فواكه = ["تفاح", "موز", "برتقال"];
لكل $فاكهة في $فواكه {
    قول ليهو($فاكهة);
}
```

### دوال
```
دالة جمع(أ, ب) {
    ارجع أ + ب;
}
$النتيجة = جيب لي جمع(5, 3);
قول ليهو($النتيجة);
```

## تشغيل الأمثلة

```bash
# مثال بسيط
python havnix.py examples/hello.havnix

# نظام درجات
python havnix.py examples/grade_system.havnix

# مولد كلمات مرور
python havnix.py examples/password_generator.havnix

# آلة حاسبة
python havnix.py examples/calculator.havnix

# تطبيق سطح مكتب
python havnix.py examples/desktop_app.havnix
```

## حل المشاكل

### "python غير موجود"
- تأكد من تثبيت Python وإضافته لـ PATH
- على Windows: استخدم `py` بدلاً من `python`

### "خطأ في الترميز"
```bash
# تأكد من استخدام UTF-8
export PYTHONIOENCODING=utf-8
```

### "المنفذ 8585 مستخدم"
```bash
# استخدم منفذ مختلف
python ide.py 9090
```
