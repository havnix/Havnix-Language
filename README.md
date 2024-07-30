# Havnix Language

لغة برمجة عربية باللهجة السودانية مطورة بواسطة المبرمج Osman Salih.

## المقدمة

Havnix هي لغة برمجة بسيطة ومباشرة، تستخدم اللغة العربية باللهجة السودانية لتنفيذ الأوامر. تم تصميمها لتكون سهلة الفهم والاستخدام لمن يتحدثون اللغة العربية، وخاصة باللهجة السودانية.

## البداية

### المتطلبات

- Python 3.x

### كيفية الاستخدام

1. **تنصيب Python**:
   تأكد من أن لديك Python مثبتًا على جهازك. يمكنك تنزيله من [python.org](https://www.python.org/).

2. **تنزيل مترجم Havnix**:
   قم بتنزيل الكود من المستودع على GitHub:
   ```sh
   git clone https://github.com/havnix/Havnix-Language.git
   ```


إنشاء ملف Havnix:

أنشئ ملفًا جديدًا بامتداد .havnix وضع فيه كود Havnix.

تشغيل لغة البرمجة:
افتح سطر الأوامر وانتقل إلى المجلد الذي يحتوي على ملف البايثون والملف الذي أنشأته بلغة Havnix، ثم نفذ الأمر التالي:
```
python havnix.py <اسم الملف>.havnix
```

او قم بتشغيل ملف run.bat بعد تعديله ووضع اسم ملف Havnix الذي قمت بإنشائه


إليك مثالًا بسيطًا لملف Havnix:

```havnix

/* 
Powered By Osman Salih
Havnix Language v1.0.0
All Rights Reserved (GPL-3.0 license)

‣ Important | If you can help you can contribute in github https://github.com/havnix/Havnix-Language/
*/

// متغيرات

$الاسم = "Osman";
$العمر = 18;
$سوداني = صاح;
$مصفوفة = [1, 2, 3, 4, 5];

// تنفيذ

قول ليهو("=-=-=-=-=-=-=-=-=-=");
قول ليهو("Havnix Language (Developed By: Osman Salih)");
قول ليهو("Made In Sudan <3");
قول ليهو("=-=-=-=-=-=-=-=-=-=");

لو (18 == 18) {
    قول ليهو("Your age is $العمر");
}

لو ($الاسم == "Osman") {
    قول ليهو("Your name is $الاسم");
}

لو ($سوداني == صاح) {
    قول ليهو("You're Sudanese");
}
غير كدا {
	قول ليهو("You're not Sudanese");
}

قول ليهو("$مصفوفة");
قول ليهو("You choosed this value from the array: $مصفوفة[3].");

```

الأوامر المدعومة
قول ليهو: لطباعة النصوص على الشاشة.

```havnix
قول ليهو("نص للطباعة");

```

المتغيرات: تعريف المتغيرات والمصفوفات.


```havnix
$متغير = "قيمة";
$مصفوفة = [1, 2, 3, 4];
```

الجمل الشرطية: تنفيذ الشروط.

```havnix
لو ($متغير == "قيمة") {
    قول ليهو("الشروط محققة");
}
غير كدا {
    قول ليهو("الشروط ما محققة");
}
```


إذا كنت ترغب في المساعدة في تطوير اللغة، يمكنك المساهمة على GitHub سواء ب Pull Requests أو الابلاغ عن المشاكل.


```
Powered By Havnix™
Developed By Osman Salih
All Rights Reserved (GPL-3.0 license)
```
