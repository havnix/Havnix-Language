<?php $page_title = 'الدوال المدمجة - Havnix'; ?>

<div class="container">
    <div class="docs-layout">
        <?php include INCLUDES_PATH . '/docs-sidebar.php'; ?>

        <div class="docs-content">
            <h1>⚡ الدوال المدمجة</h1>
            <p>هافنيكس تأتي مع أكثر من 30 دالة مدمجة جاهزة للاستخدام.</p>

            <h2>دوال النصوص</h2>
            <table class="docs-table">
                <tr><th>الدالة</th><th>الوصف</th><th>المثال</th></tr>
                <tr><td><code>طول(نص)</code></td><td>طول النص</td><td><code>طول("مرحبا")</code> → <code>5</code></td></tr>
                <tr><td><code>قطع(نص, بداية, نهاية)</code></td><td>جزء من النص</td><td><code>قطع("مرحبا", 0, 3)</code></td></tr>
                <tr><td><code>بدل(نص, قديم, جديد)</code></td><td>استبدال</td><td><code>بدل("أهلا", "أ", "ب")</code></td></tr>
                <tr><td><code>قسم(نص, فاصل)</code></td><td>تقسيم لقائمة</td><td><code>قسم("أ ب ج", " ")</code></td></tr>
                <tr><td><code>كبر(نص)</code></td><td>أحرف كبيرة</td><td><code>كبر("hello")</code> → <code>"HELLO"</code></td></tr>
                <tr><td><code>صغر(نص)</code></td><td>أحرف صغيرة</td><td><code>صغر("HELLO")</code> → <code>"hello"</code></td></tr>
                <tr><td><code>فيهو(نص, جزء)</code></td><td>هل يحتوي</td><td><code>فيهو("مرحبا", "حب")</code> → <code>صاح</code></td></tr>
                <tr><td><code>ضم(قائمة, فاصل)</code></td><td>دمج لنص</td><td><code>ضم(["أ","ب"], "-")</code></td></tr>
            </table>

            <h2>دوال الرياضيات</h2>
            <table class="docs-table">
                <tr><th>الدالة</th><th>الوصف</th><th>المثال</th></tr>
                <tr><td><code>جذر(رقم)</code></td><td>الجذر التربيعي</td><td><code>جذر(16)</code> → <code>4</code></td></tr>
                <tr><td><code>قوة(أساس, أس)</code></td><td>الأس</td><td><code>قوة(2, 3)</code> → <code>8</code></td></tr>
                <tr><td><code>مطلق(رقم)</code></td><td>القيمة المطلقة</td><td><code>مطلق(-5)</code> → <code>5</code></td></tr>
                <tr><td><code>تقريب(رقم)</code></td><td>التقريب</td><td><code>تقريب(3.7)</code> → <code>4</code></td></tr>
                <tr><td><code>اقصى(أ, ب)</code></td><td>الأكبر</td><td><code>اقصى(5, 10)</code> → <code>10</code></td></tr>
                <tr><td><code>ادنى(أ, ب)</code></td><td>الأصغر</td><td><code>ادنى(5, 10)</code> → <code>5</code></td></tr>
                <tr><td><code>مجموع(قائمة)</code></td><td>مجموع القائمة</td><td><code>مجموع([1,2,3])</code> → <code>6</code></td></tr>
                <tr><td><code>عشوائي(حد_أدنى, حد_أقصى)</code></td><td>رقم عشوائي</td><td><code>عشوائي(1, 100)</code></td></tr>
            </table>

            <h2>دوال القوائم</h2>
            <table class="docs-table">
                <tr><th>الدالة</th><th>الوصف</th><th>المثال</th></tr>
                <tr><td><code>اضف(قائمة, عنصر)</code></td><td>إضافة</td><td><code>اضف($ق, 5)</code></td></tr>
                <tr><td><code>احذف(قائمة, فهرس)</code></td><td>حذف</td><td><code>احذف($ق, 0)</code></td></tr>
                <tr><td><code>ادرج(قائمة, فهرس, عنصر)</code></td><td>إدراج</td><td><code>ادرج($ق, 1, "ب")</code></td></tr>
                <tr><td><code>ترتيب(قائمة)</code></td><td>ترتيب</td><td><code>ترتيب([3,1,2])</code></td></tr>
                <tr><td><code>عكس(قائمة)</code></td><td>عكس</td><td><code>عكس([1,2,3])</code></td></tr>
            </table>

            <h2>دوال القواميس</h2>
            <table class="docs-table">
                <tr><th>الدالة</th><th>الوصف</th></tr>
                <tr><td><code>مفاتيح(قاموس)</code></td><td>قائمة بالمفاتيح</td></tr>
                <tr><td><code>قيم(قاموس)</code></td><td>قائمة بالقيم</td></tr>
                <tr><td><code>عناصر(قاموس)</code></td><td>قائمة بأزواج [مفتاح، قيمة]</td></tr>
            </table>

            <h2>دوال التحويل</h2>
            <table class="docs-table">
                <tr><th>الدالة</th><th>الوصف</th><th>المثال</th></tr>
                <tr><td><code>رقم(نص)</code></td><td>تحويل لرقم</td><td><code>رقم("42")</code> → <code>42</code></td></tr>
                <tr><td><code>نص(رقم)</code></td><td>تحويل لنص</td><td><code>نص(42)</code> → <code>"42"</code></td></tr>
                <tr><td><code>عشري(نص)</code></td><td>تحويل لعشري</td><td><code>عشري("3.14")</code></td></tr>
                <tr><td><code>نوع(قيمة)</code></td><td>نوع البيان</td><td><code>نوع(42)</code> → <code>"رقم"</code></td></tr>
            </table>

            <h2>دوال الملفات</h2>
            <table class="docs-table">
                <tr><th>الدالة</th><th>الوصف</th></tr>
                <tr><td><code>اقرأ_ملف("مسار")</code></td><td>قراءة محتوى ملف</td></tr>
                <tr><td><code>اكتب_ملف("مسار", محتوى)</code></td><td>كتابة في ملف</td></tr>
                <tr><td><code>ضيف_ملف("مسار", محتوى)</code></td><td>إضافة لنهاية ملف</td></tr>
                <tr><td><code>احذف_ملف("مسار")</code></td><td>حذف ملف</td></tr>
            </table>

            <h2>دوال JSON</h2>
            <div class="code-block">
                <pre><span class="cm">// تحويل من JSON</span>
<span class="var">$بيانات</span> <span class="op">=</span> <span class="fn">من_json</span>(<span class="str">'{"الاسم": "أحمد"}'</span>)<span class="op">;</span>

<span class="cm">// تحويل إلى JSON</span>
<span class="var">$نص</span> <span class="op">=</span> <span class="fn">الى_json</span>(<span class="var">$بيانات</span>)<span class="op">;</span></pre>
            </div>

            <h2>دوال أخرى</h2>
            <table class="docs-table">
                <tr><th>الدالة</th><th>الوصف</th></tr>
                <tr><td><code>الوقت_الحالي()</code></td><td>الوقت الحالي كنص</td></tr>
                <tr><td><code>انتظر(ثواني)</code></td><td>توقف مؤقت</td></tr>
                <tr><td><code>اسأل("سؤال")</code></td><td>طلب إدخال من المستخدم</td></tr>
            </table>

            <div style="margin-top: 40px; padding: 20px; background: var(--surface-light); border-radius: 10px; border-right: 4px solid var(--accent);">
                <p><strong>التالي:</strong> تعلم عن <a href="<?php echo SITE_URL; ?>/docs/advanced">الميزات المتقدمة</a> مثل MySQL وAPIs وواجهات سطح المكتب</p>
            </div>
        </div>
    </div>
</div>
