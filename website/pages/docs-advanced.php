<?php $page_title = 'الميزات المتقدمة - Havnix'; ?>

<div class="container">
    <div class="docs-layout">
        <?php include INCLUDES_PATH . '/docs-sidebar.php'; ?>

        <div class="docs-content">
            <h1><i class="fas fa-fire"></i> الميزات المتقدمة</h1>

            <h2>قواعد بيانات MySQL</h2>
            <p>هافنيكس تدعم الاتصال بقواعد بيانات MySQL وتنفيذ الاستعلامات مباشرة.</p>

            <h3>الاتصال بقاعدة البيانات</h3>
            <div class="code-block">
                <pre><span class="var">$قاعدة</span> <span class="op">=</span> <span class="fn">اتصل_قاعدة</span>(<span class="str">"localhost"</span><span class="op">,</span> <span class="str">"root"</span><span class="op">,</span> <span class="str">"password"</span><span class="op">,</span> <span class="str">"mydb"</span>)<span class="op">;</span></pre>
            </div>

            <h3>استعلام (SELECT)</h3>
            <div class="code-block">
                <pre><span class="var">$نتائج</span> <span class="op">=</span> <span class="fn">استعلم</span>(<span class="var">$قاعدة</span><span class="op">,</span> <span class="str">"SELECT * FROM users"</span>)<span class="op">;</span>
<span class="kw">لكل</span> <span class="var">$صف</span> <span class="kw">في</span> <span class="var">$نتائج</span> {
    <span class="fn">قول ليهو</span>(<span class="var">$صف</span>)<span class="op">;</span>
}</pre>
            </div>

            <h3>تنفيذ أوامر (INSERT, UPDATE, DELETE)</h3>
            <div class="code-block">
                <pre><span class="fn">نفذ_استعلام</span>(<span class="var">$قاعدة</span><span class="op">,</span> <span class="str">"INSERT INTO users (name, age) VALUES ('أحمد', 25)"</span>)<span class="op">;</span>
<span class="fn">نفذ_استعلام</span>(<span class="var">$قاعدة</span><span class="op">,</span> <span class="str">"UPDATE users SET age = 26 WHERE name = 'أحمد'"</span>)<span class="op">;</span>
<span class="fn">نفذ_استعلام</span>(<span class="var">$قاعدة</span><span class="op">,</span> <span class="str">"DELETE FROM users WHERE name = 'أحمد'"</span>)<span class="op">;</span></pre>
            </div>

            <h3>إغلاق الاتصال</h3>
            <div class="code-block">
                <pre><span class="fn">اقفل_قاعدة</span>(<span class="var">$قاعدة</span>)<span class="op">;</span></pre>
            </div>

            <h2>التعامل مع APIs</h2>

            <h3>طلب GET</h3>
            <div class="code-block">
                <pre><span class="var">$رد</span> <span class="op">=</span> <span class="fn">جيب_من</span>(<span class="str">"https://api.example.com/users"</span>)<span class="op">;</span>
<span class="fn">اطبع</span>(<span class="var">$رد</span>)<span class="op">;</span></pre>
            </div>

            <h3>طلب POST</h3>
            <div class="code-block">
                <pre><span class="var">$بيانات</span> <span class="op">=</span> {<span class="str">"الاسم"</span><span class="op">:</span> <span class="str">"عثمان"</span><span class="op">,</span> <span class="str">"العمر"</span><span class="op">:</span> <span class="num">18</span>}<span class="op">;</span>
<span class="var">$رد</span> <span class="op">=</span> <span class="fn">رسل_لي</span>(<span class="str">"https://api.example.com/users"</span><span class="op">,</span> <span class="var">$بيانات</span>)<span class="op">;</span></pre>
            </div>

            <h3>طلب PUT</h3>
            <div class="code-block">
                <pre><span class="var">$رد</span> <span class="op">=</span> <span class="fn">حدث_في</span>(<span class="str">"https://api.example.com/users/1"</span><span class="op">,</span> <span class="var">$بيانات</span>)<span class="op">;</span></pre>
            </div>

            <h3>طلب DELETE</h3>
            <div class="code-block">
                <pre><span class="var">$رد</span> <span class="op">=</span> <span class="fn">احذف_من_api</span>(<span class="str">"https://api.example.com/users/1"</span>)<span class="op">;</span></pre>
            </div>

            <h2>واجهات سطح المكتب (GUI)</h2>
            <p>هافنيكس تدعم إنشاء تطبيقات سطح مكتب رسومية باستخدام tkinter.</p>

            <h3>إنشاء نافذة</h3>
            <div class="code-block">
                <pre><span class="var">$نافذتي</span> <span class="op">=</span> <span class="fn">نافذة_جديدة</span>(<span class="str">"تطبيقي الأول"</span><span class="op">,</span> <span class="num">600</span><span class="op">,</span> <span class="num">400</span>)<span class="op">;</span></pre>
            </div>

            <h3>إضافة عناصر</h3>
            <div class="code-block">
                <pre><span class="cm">// نص ثابت</span>
<span class="fn">نص_ثابت</span>(<span class="var">$نافذتي</span><span class="op">,</span> <span class="str">"مرحبا بك!"</span>)<span class="op">;</span>

<span class="cm">// زر</span>
<span class="fn">زر</span>(<span class="var">$نافذتي</span><span class="op">,</span> <span class="str">"اضغط هنا"</span>)<span class="op">;</span>

<span class="cm">// مدخل نص</span>
<span class="var">$اسم</span> <span class="op">=</span> <span class="fn">مدخل_نص</span>(<span class="var">$نافذتي</span><span class="op">,</span> <span class="num">30</span>)<span class="op">;</span>

<span class="cm">// مساحة نص</span>
<span class="var">$محرر</span> <span class="op">=</span> <span class="fn">مساحة_نص</span>(<span class="var">$نافذتي</span><span class="op">,</span> <span class="num">10</span><span class="op">,</span> <span class="num">40</span>)<span class="op">;</span>

<span class="cm">// قائمة اختيار</span>
<span class="var">$خيارات</span> <span class="op">=</span> [<span class="str">"الخيار 1"</span><span class="op">,</span> <span class="str">"الخيار 2"</span><span class="op">,</span> <span class="str">"الخيار 3"</span>]<span class="op">;</span>
<span class="var">$قائمة</span> <span class="op">=</span> <span class="fn">قائمة_اختيار</span>(<span class="var">$نافذتي</span><span class="op">,</span> <span class="var">$خيارات</span>)<span class="op">;</span>

<span class="cm">// خانة اختيار</span>
<span class="var">$موافق</span> <span class="op">=</span> <span class="fn">خانة_اختيار</span>(<span class="var">$نافذتي</span><span class="op">,</span> <span class="str">"أوافق"</span>)<span class="op">;</span></pre>
            </div>

            <h3>تشغيل النافذة</h3>
            <div class="code-block">
                <pre><span class="fn">شغل_واجهة</span>(<span class="var">$نافذتي</span>)<span class="op">;</span></pre>
            </div>

            <h3>مثال كامل: آلة حاسبة</h3>
            <div class="code-block">
                <pre><span class="var">$نافذة</span> <span class="op">=</span> <span class="fn">نافذة_جديدة</span>(<span class="str">"آلة حاسبة"</span><span class="op">,</span> <span class="num">300</span><span class="op">,</span> <span class="num">200</span>)<span class="op">;</span>
<span class="fn">نص_ثابت</span>(<span class="var">$نافذة</span><span class="op">,</span> <span class="str">"الرقم الأول:"</span>)<span class="op">;</span>
<span class="var">$رقم1</span> <span class="op">=</span> <span class="fn">مدخل_نص</span>(<span class="var">$نافذة</span><span class="op">,</span> <span class="num">20</span>)<span class="op">;</span>
<span class="fn">نص_ثابت</span>(<span class="var">$نافذة</span><span class="op">,</span> <span class="str">"الرقم الثاني:"</span>)<span class="op">;</span>
<span class="var">$رقم2</span> <span class="op">=</span> <span class="fn">مدخل_نص</span>(<span class="var">$نافذة</span><span class="op">,</span> <span class="num">20</span>)<span class="op">;</span>
<span class="fn">زر</span>(<span class="var">$نافذة</span><span class="op">,</span> <span class="str">"احسب"</span>)<span class="op">;</span>
<span class="fn">شغل_واجهة</span>(<span class="var">$نافذة</span>)<span class="op">;</span></pre>
            </div>

            <h2>استيراد ملفات</h2>
            <div class="code-block">
                <pre><span class="cm">// استيراد ملف هافنيكس آخر</span>
<span class="kw">استورد</span> <span class="str">"helpers.havnix"</span><span class="op">;</span></pre>
            </div>

            <div style="margin-top: 40px; padding: 20px; background: var(--surface-light); border-radius: 10px; border-right: 4px solid var(--accent);">
                <p><strong>نصيحة:</strong> شوف <a href="https://github.com/Snixrs/Havnix-Language/tree/main/examples" target="_blank">مجلد الأمثلة على GitHub</a> لبرامج كاملة تشتغل</p>
            </div>
        </div>
    </div>
</div>
