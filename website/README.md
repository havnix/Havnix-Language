# Havnix Website

الموقع الرسمي للغة هافنيكس - لغة برمجة عربية سودانية.

## الصفحات

| المسار | الصفحة | الوصف |
|--------|--------|-------|
| `/` | الرئيسية | Landing page مع ميزات اللغة |
| `/docs` | التوثيق | نظرة عامة على التوثيق |
| `/docs/start` | البداية السريعة | المتغيرات، الشروط، الحلقات، الدوال |
| `/docs/syntax` | بنية اللغة | أنواع البيانات والعمليات والكلمات المفتاحية |
| `/docs/functions` | الدوال المدمجة | 30+ دالة جاهزة |
| `/docs/advanced` | المتقدمة | MySQL, APIs, GUI |
| `/download` | تحميل | روابط تحميل لكل نظام تشغيل |
| `/marketplace` | المكتبات | Marketplace مع نظام رفع وموافقة |
| `/about` | حول | معلومات عن المشروع |

## التقنيات

- **Backend:** PHP 7.4+
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Database:** MySQL 5.7+ / MariaDB
- **URL Routing:** Apache mod_rewrite (.htaccess)

## التثبيت

### 1. متطلبات

- PHP 7.4 أو أعلى
- MySQL 5.7 أو أعلى (اختياري - يعمل بدونه)
- Apache مع mod_rewrite

### 2. إعداد قاعدة البيانات (اختياري)

```bash
mysql -u root -p < database.sql
```

### 3. التكوين

عدّل `config.php` (اختياري - الموقع يكتشف المسار تلقائياً):

```php
define('DB_HOST', 'localhost');
define('DB_NAME', 'havnix_db');
define('DB_USER', 'root');
define('DB_PASS', 'your_password');
```

> ملاحظة: `SITE_URL` يتم اكتشافه تلقائياً - لا حاجة لتعديله.

### 4. التشغيل على XAMPP (موصى به)

1. انسخ مجلد `website` إلى `C:\xampp\htdocs\havnix\`
2. شغّل Apache من لوحة XAMPP
3. افتح المتصفح: `http://localhost/havnix/`

> **ملاحظة:** تأكد من تفعيل `mod_rewrite` في Apache. في XAMPP، افتح `httpd.conf` وتأكد من وجود:
> ```
> LoadModule rewrite_module modules/mod_rewrite.so
> ```
> وأن `AllowOverride All` مفعّل لمجلد htdocs.

### 5. التشغيل بدون XAMPP

```bash
cd website
php -S localhost:8080 router.php
```

ثم افتح: http://localhost:8080

## هيكل الملفات

```
website/
├── index.php          # الراوتر الرئيسي
├── config.php         # التكوين
├── database.sql       # مخطط قاعدة البيانات
├── .htaccess          # إعادة توجيه URLs
├── assets/
│   ├── css/
│   │   └── style.css  # الأنماط
│   ├── js/
│   │   └── main.js    # JavaScript
│   └── images/
├── includes/
│   ├── header.php     # الرأس
│   ├── footer.php     # التذييل
│   └── docs-sidebar.php
├── pages/
│   ├── home.php       # الرئيسية
│   ├── docs.php       # التوثيق
│   ├── docs-start.php
│   ├── docs-syntax.php
│   ├── docs-functions.php
│   ├── docs-advanced.php
│   ├── download.php   # التحميل
│   ├── marketplace.php # المكتبات
│   ├── about.php      # حول
│   └── 404.php        # خطأ 404
├── api/
│   ├── packages.php   # API المكتبات
│   └── upload.php     # رفع مكتبة
└── uploads/
    └── packages/      # ملفات المكتبات المرفوعة
```

## البراند

- **الاسم:** Havnix
- **الشعار:** أبيض على خلفية Gradient (أسود → #1B569A)
- **الخط:** Segoe UI / Noto Sans Arabic
