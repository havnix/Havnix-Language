<?php $page_title = 'Havnix - لغة برمجة عربية سودانية'; ?>

<!-- Hero -->
<section class="hero">
    <div class="hero-content">
        <span class="hero-badge">🇸🇩 الإصدار <?php echo SITE_VERSION; ?> متاح الآن</span>
        <h1>برمج بالسودانية مع هافنيكس</h1>
        <p>لغة برمجة كاملة بالعربية السودانية. اكتب كود بلغتك الأم، ابني تطبيقات سطح مكتب، اتصل بقواعد بيانات، وتعامل مع APIs.</p>

        <div class="hero-buttons">
            <a href="<?php echo SITE_URL; ?>/download" class="btn btn-primary">⬇ حمّل الآن</a>
            <a href="<?php echo SITE_URL; ?>/docs/start" class="btn btn-outline">📖 ابدأ التعلم</a>
        </div>

        <div class="hero-code">
            <pre><span class="cm">// مرحبا بك في هافنيكس!</span>
<span class="var">$الاسم</span> <span class="op">=</span> <span class="str">"عثمان"</span><span class="op">;</span>
<span class="var">$العمر</span> <span class="op">=</span> <span class="num">18</span><span class="op">;</span>

<span class="fn">قول ليهو</span>(<span class="str">"مرحبا يا <span class="var">$الاسم</span>!"</span>)<span class="op">;</span>

<span class="kw">لو</span> (<span class="var">$العمر</span> <span class="op">>=</span> <span class="num">18</span>) {
    <span class="fn">قول ليهو</span>(<span class="str">"انت كبير 💪"</span>)<span class="op">;</span>
}</pre>
        </div>
    </div>
</section>

<!-- Features -->
<section class="features">
    <div class="container">
        <h2 class="section-title">ميزات قوية بلغتك</h2>
        <p class="section-subtitle">هافنيكس مش بس لغة برمجة بسيطة - دي لغة كاملة فيها كل شي بتحتاجو</p>

        <div class="features-grid">
            <div class="feature-card">
                <div class="feature-icon">🖥️</div>
                <h3>تطبيقات سطح مكتب</h3>
                <p>صمم واجهات رسومية كاملة بأزرار ونصوص ومدخلات وقوائم منسدلة - كل شي بالعربي.</p>
            </div>

            <div class="feature-card">
                <div class="feature-icon">🗄️</div>
                <h3>قواعد بيانات MySQL</h3>
                <p>اتصل بقواعد البيانات، نفذ استعلامات، واعمل عمليات CRUD كاملة بأوامر عربية.</p>
            </div>

            <div class="feature-card">
                <div class="feature-icon">🌐</div>
                <h3>تعامل مع APIs</h3>
                <p>ارسل طلبات GET, POST, PUT, DELETE لأي API. اجلب بيانات من الإنترنت بسهولة.</p>
            </div>

            <div class="feature-card">
                <div class="feature-icon">📝</div>
                <h3>IDE متكامل</h3>
                <p>بيئة تطوير مدمجة مع تلوين الكود، مستكشف ملفات، طرفية تفاعلية، ودعم Git.</p>
            </div>

            <div class="feature-card">
                <div class="feature-icon">📦</div>
                <h3>مكتبات مجتمعية</h3>
                <p>استخدم مكتبات جاهزة من المجتمع أو ارفع مكتبتك الخاصة ليستفيد منها الآخرون.</p>
            </div>

            <div class="feature-card">
                <div class="feature-icon">🔧</div>
                <h3>30+ دالة مدمجة</h3>
                <p>نصوص، رياضيات، ملفات، JSON، تواريخ - كل الأدوات اللي بتحتاجها موجودة.</p>
            </div>
        </div>
    </div>
</section>

<!-- Quick Example -->
<section style="padding: 80px 0; background: var(--bg-dark);">
    <div class="container">
        <h2 class="section-title">شوف كيف سهل</h2>
        <p class="section-subtitle">كل أمر بالعربي. ما في داعي تتعلم إنجليزي عشان تبرمج.</p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 24px;">
            <div>
                <h3 style="margin-bottom: 12px; color: var(--accent);">📋 قوائم وحلقات</h3>
                <div class="code-block">
                    <pre><span class="var">$فواكه</span> <span class="op">=</span> [<span class="str">"تفاح"</span><span class="op">,</span> <span class="str">"موز"</span><span class="op">,</span> <span class="str">"برتقال"</span>]<span class="op">;</span>
<span class="kw">لكل</span> <span class="var">$فاكهة</span> <span class="kw">في</span> <span class="var">$فواكه</span> {
    <span class="fn">قول ليهو</span>(<span class="var">$فاكهة</span>)<span class="op">;</span>
}</pre>
                </div>
            </div>

            <div>
                <h3 style="margin-bottom: 12px; color: var(--accent);">⚡ دوال</h3>
                <div class="code-block">
                    <pre><span class="kw">دالة</span> <span class="fn">جمع</span>(أ<span class="op">,</span> ب) {
    <span class="kw">ارجع</span> أ <span class="op">+</span> ب<span class="op">;</span>
}
<span class="var">$النتيجة</span> <span class="op">=</span> <span class="fn">جيب لي</span> <span class="fn">جمع</span>(<span class="num">5</span><span class="op">,</span> <span class="num">3</span>)<span class="op">;</span>
<span class="fn">قول ليهو</span>(<span class="var">$النتيجة</span>)<span class="op">;</span>  <span class="cm">// 8</span></pre>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- CTA -->
<section style="padding: 80px 0; background: var(--bg-gradient); text-align: center;">
    <div class="container">
        <h2 style="font-size: 36px; margin-bottom: 16px;">جاهز تبدأ؟</h2>
        <p style="color: var(--text-light); margin-bottom: 32px; font-size: 18px;">حمّل هافنيكس مجاناً وابدأ البرمجة بالسودانية الحين</p>
        <div class="hero-buttons">
            <a href="<?php echo SITE_URL; ?>/download" class="btn btn-primary">⬇ حمّل مجاناً</a>
            <a href="https://github.com/Snixrs/Havnix-Language" target="_blank" class="btn btn-outline">⭐ GitHub</a>
        </div>
    </div>
</section>
