<?php $page_title = 'البداية السريعة - Havnix'; ?>

<div class="container">
    <div class="docs-layout">
        <?php include INCLUDES_PATH . '/docs-sidebar.php'; ?>

        <div class="docs-content">
            <h1><i class="fas fa-rocket"></i> البداية السريعة</h1>

            <h2>المتغيرات</h2>
            <p>كل متغير يبدأ بعلامة <code>$</code></p>
            <div class="code-block">
                <pre><span class="var">$الاسم</span> <span class="op">=</span> <span class="str">"أحمد"</span><span class="op">;</span>
<span class="var">$العمر</span> <span class="op">=</span> <span class="num">25</span><span class="op">;</span>
<span class="var">$طالب</span> <span class="op">=</span> <span class="kw">صاح</span><span class="op">;</span>
<span class="var">$درجات</span> <span class="op">=</span> [<span class="num">95</span><span class="op">,</span> <span class="num">87</span><span class="op">,</span> <span class="num">92</span>]<span class="op">;</span></pre>
            </div>

            <h3>الثوابت</h3>
            <div class="code-block">
                <pre><span class="kw">ثابت</span> <span class="var">$PI</span> <span class="op">=</span> <span class="num">3.14159</span><span class="op">;</span>
<span class="cm">// $PI = 5;  ← خطأ! الثابت ما بتغير</span></pre>
            </div>

            <h2>الطباعة</h2>
            <div class="code-block">
                <pre><span class="fn">قول ليهو</span>(<span class="str">"مرحبا يا <span class="var">$الاسم</span>!"</span>)<span class="op">;</span>
<span class="fn">قول ليهو</span>(<span class="str">"عمرك <span class="var">$العمر</span> سنة"</span>)<span class="op">;</span>
<span class="fn">اطبع</span>(<span class="var">$درجات</span>)<span class="op">;</span></pre>
            </div>

            <h2>الشروط</h2>
            <div class="code-block">
                <pre><span class="kw">لو</span> (<span class="var">$العمر</span> <span class="op">>=</span> <span class="num">18</span>) {
    <span class="fn">قول ليهو</span>(<span class="str">"كبير"</span>)<span class="op">;</span>
} <span class="kw">غير كدا لو</span> (<span class="var">$العمر</span> <span class="op">>=</span> <span class="num">13</span>) {
    <span class="fn">قول ليهو</span>(<span class="str">"مراهق"</span>)<span class="op">;</span>
} <span class="kw">غير كدا</span> {
    <span class="fn">قول ليهو</span>(<span class="str">"صغير"</span>)<span class="op">;</span>
}</pre>
            </div>

            <h2>الحلقات</h2>

            <h3>حلقة طالما (while)</h3>
            <div class="code-block">
                <pre><span class="var">$ع</span> <span class="op">=</span> <span class="num">1</span><span class="op">;</span>
<span class="kw">طالما</span> (<span class="var">$ع</span> <span class="op">&lt;=</span> <span class="num">5</span>) {
    <span class="fn">قول ليهو</span>(<span class="var">$ع</span>)<span class="op">;</span>
    <span class="var">$ع</span> <span class="op">=</span> <span class="var">$ع</span> <span class="op">+</span> <span class="num">1</span><span class="op">;</span>
}</pre>
            </div>

            <h3>حلقة لكل (foreach)</h3>
            <div class="code-block">
                <pre><span class="var">$فواكه</span> <span class="op">=</span> [<span class="str">"تفاح"</span><span class="op">,</span> <span class="str">"موز"</span><span class="op">,</span> <span class="str">"برتقال"</span>]<span class="op">;</span>
<span class="kw">لكل</span> <span class="var">$فاكهة</span> <span class="kw">في</span> <span class="var">$فواكه</span> {
    <span class="fn">قول ليهو</span>(<span class="str">"فاكهة: <span class="var">$فاكهة</span>"</span>)<span class="op">;</span>
}</pre>
            </div>

            <h2>الدوال</h2>
            <div class="code-block">
                <pre><span class="kw">دالة</span> <span class="fn">مرحبا</span>(الاسم) {
    <span class="fn">قول ليهو</span>(<span class="str">"أهلاً يا <span class="var">$الاسم</span>!"</span>)<span class="op">;</span>
}

<span class="fn">جيب لي</span> <span class="fn">مرحبا</span>(<span class="str">"عثمان"</span>)<span class="op">;</span>

<span class="cm">// دالة مع قيمة مرجعة</span>
<span class="kw">دالة</span> <span class="fn">مربع</span>(ن) {
    <span class="kw">ارجع</span> ن <span class="op">*</span> ن<span class="op">;</span>
}
<span class="var">$نتيجة</span> <span class="op">=</span> <span class="fn">جيب لي</span> <span class="fn">مربع</span>(<span class="num">7</span>)<span class="op">;</span></pre>
            </div>

            <h2>معالجة الأخطاء</h2>
            <div class="code-block">
                <pre><span class="kw">جرب</span> {
    <span class="var">$نتيجة</span> <span class="op">=</span> <span class="num">10</span> <span class="op">/</span> <span class="num">0</span><span class="op">;</span>
} <span class="kw">امسك</span> {
    <span class="fn">قول ليهو</span>(<span class="str">"حصل خطأ!"</span>)<span class="op">;</span>
} <span class="kw">واخيراً</span> {
    <span class="fn">قول ليهو</span>(<span class="str">"تم"</span>)<span class="op">;</span>
}</pre>
            </div>

            <div style="margin-top: 40px; padding: 20px; background: var(--surface-light); border-radius: 10px; border-right: 4px solid var(--accent);">
                <p><strong>الخطوة التالية:</strong> تعلم المزيد عن <a href="<?php echo SITE_URL; ?>/docs/syntax">بنية اللغة</a> أو اطلع على <a href="<?php echo SITE_URL; ?>/docs/functions">الدوال المدمجة</a></p>
            </div>
        </div>
    </div>
</div>
