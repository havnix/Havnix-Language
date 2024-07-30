# Havnix Language | لغة هافنيكس

## المقدمة

Havnix هي لغة برمجة بسيطة ومباشرة، تستخدم اللغة العربية باللهجة السودانية لتنفيذ الأوامر. تم تصميمها لتكون سهلة الفهم والاستخدام لمن يتحدثون اللغة العربية، وخاصة باللهجة السودانية.
تم تطويرها بواسطة المبرمج [Osman Salih](https://github.com/osmansalih)

### المتطلبات

- Python 3.x

### كيفية الاستخدام

1. **تنصيب Python**
   تأكد من أن لديك Python مثبتًا على جهازك. يمكنك تنزيله من [python.org](https://www.python.org/).

2. **تنزيل لغة Havnix**

   قم بتنزيل الكود من المستودع على GitHub:
   ```sh
   git clone https://github.com/havnix/Havnix-Language.git
   ```

3. **تعلم استخدام لغة Havnix**
   
   لمعرفة طريقة البرمجة بلغة Havnix اتبع التعليمات [من هنا](https://github.com/havnix/Havnix-Language/wiki).



إنشاء ملف Havnix:

أنشئ ملفًا جديدًا بامتداد .havnix وضع فيه كود Havnix.

تشغيل لغة البرمجة:
افتح سطر الأوامر وانتقل إلى المجلد الذي يحتوي على ملف البايثون والملف الذي أنشأته بلغة Havnix، ثم نفذ الأمر التالي:
```
python havnix.py <اسم الملف>.havnix
```

او قم بتشغيل ملف run.bat بعد تعديله ووضع اسم ملف Havnix الذي قمت بإنشائه

مثال لملف run.bat:
```bat
@echo off
title Havnix 1.0.0 (Powered by Osman Salih)
color a

:run_program
cls
python havnix.py main.havnix
echo.
echo -----------------------
echo.
echo Press [1] to reload...
echo Press [2] to exit...
echo.
echo -----------------------
echo.
choice /c 12 /n
if errorlevel 2 goto :eof
if errorlevel 1 goto run_program
```


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


<b>إذا كنت ترغب في المساعدة في تطوير اللغة، يمكنك المساهمة على GitHub سواء ب Pull Requests أو الابلاغ عن المشاكل.</b>


```
Powered By Havnix™
Developed By Osman Salih
All Rights Reserved (GPL-3.0 license)
```
