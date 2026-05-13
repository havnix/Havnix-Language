<?php $page_title = 'المكتبات - Havnix Packages'; ?>

<div class="container">
    <div class="docs-layout">
        <?php include INCLUDES_PATH . '/docs-sidebar.php'; ?>

        <div class="docs-content">
            <h1><i class="fas fa-cubes"></i> المكتبات</h1>
            <p>هافنيكس تدعم نظام مكتبات متكامل. يمكنك تثبيت مكتبات جاهزة أو إنشاء مكتبتك الخاصة ومشاركتها مع المجتمع.</p>

            <h2><i class="fas fa-terminal"></i> مدير المكتبات (CLI)</h2>
            <p>استخدم أوامر <code>havnix</code> لإدارة المكتبات من سطر الأوامر:</p>

            <table class="docs-table">
                <tr><th>الأمر</th><th>الوصف</th></tr>
                <tr><td><code>havnix install &lt;اسم&gt;</code></td><td>تثبيت مكتبة</td></tr>
                <tr><td><code>havnix install &lt;اسم&gt;@&lt;إصدار&gt;</code></td><td>تثبيت إصدار محدد</td></tr>
                <tr><td><code>havnix uninstall &lt;اسم&gt;</code></td><td>إزالة مكتبة</td></tr>
                <tr><td><code>havnix update &lt;اسم&gt;</code></td><td>تحديث مكتبة</td></tr>
                <tr><td><code>havnix list</code></td><td>عرض المكتبات المثبتة</td></tr>
                <tr><td><code>havnix search &lt;كلمة&gt;</code></td><td>بحث عن مكتبات</td></tr>
                <tr><td><code>havnix info &lt;اسم&gt;</code></td><td>معلومات تفصيلية عن مكتبة</td></tr>
                <tr><td><code>havnix init</code></td><td>إنشاء مشروع جديد</td></tr>
            </table>

            <h2><i class="fas fa-download"></i> تثبيت مكتبة</h2>

            <h3>1. تثبيت مكتبة</h3>
            <div class="code-block" style="direction: ltr; text-align: left;">
                <pre>havnix install التقويم_الهجري</pre>
            </div>
            <p>أو مع تحديد الإصدار:</p>
            <div class="code-block" style="direction: ltr; text-align: left;">
                <pre>havnix install التقويم_الهجري@1.0.0</pre>
            </div>

            <p>هذا الأمر يقوم بـ:</p>
            <ul style="padding-right: 24px; color: var(--text-light);">
                <li>إنشاء مجلد <code>havnix_libraries/</code> في مشروعك</li>
                <li>نسخ ملفات المكتبة إلى <code>havnix_libraries/التقويم_الهجري/</code></li>
                <li>تحديث ملف <code>libraries.json</code> بالمكتبة المثبتة</li>
            </ul>

            <h3>2. استخدام المكتبة في الكود</h3>
            <div class="code-block">
                <pre><span class="kw">استورد</span> <span class="str">"havnix_libraries/التقويم_الهجري/التقويم_الهجري.havnix"</span><span class="op">;</span>

<span class="cm">// الآن يمكنك استخدام دوال المكتبة</span>
<span class="var">$تاريخ</span> <span class="op">=</span> <span class="fn">جيب لي</span> <span class="fn">ميلادي_الى_هجري</span>(<span class="num">2024</span>, <span class="num">1</span>, <span class="num">15</span>)<span class="op">;</span>
<span class="fn">قول ليهو</span>(<span class="var">$تاريخ</span>)<span class="op">;</span></pre>
            </div>

            <h2><i class="fas fa-box-open"></i> المكتبات المتوفرة</h2>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 24px 0;">
                <div class="feature-card">
                    <div class="feature-icon"><i class="fas fa-calendar-alt"></i></div>
                    <h3>التقويم_الهجري</h3>
                    <p>تحويل التواريخ الميلادية إلى هجرية، أسماء الأشهر والأيام بالعربي</p>
                    <code style="font-size: 12px;">havnix install التقويم_الهجري</code>
                </div>
                <div class="feature-card">
                    <div class="feature-icon"><i class="fas fa-calculator"></i></div>
                    <h3>الرياضيات_المتقدمة</h3>
                    <p>قوة، مضروب، متوسط، وسيط، أعداد أولية، فيبوناتشي، ق.م.أ</p>
                    <code style="font-size: 12px;">havnix install الرياضيات_المتقدمة</code>
                </div>
                <div class="feature-card">
                    <div class="feature-icon"><i class="fas fa-font"></i></div>
                    <h3>معالج_النصوص</h3>
                    <p>عكس نص، عد كلمات، بحث، اقتطاع، تنظيف، دمج نصوص</p>
                    <code style="font-size: 12px;">havnix install معالج_النصوص</code>
                </div>
                <div class="feature-card">
                    <div class="feature-icon"><i class="fas fa-palette"></i></div>
                    <h3>الألوان</h3>
                    <p>طباعة ملونة في الطرفية، رسائل نجاح وخطأ وتحذير مزخرفة</p>
                    <code style="font-size: 12px;">havnix install الألوان</code>
                </div>
                <div class="feature-card">
                    <div class="feature-icon"><i class="fas fa-check-double"></i></div>
                    <h3>التحقق</h3>
                    <p>تحقق من بريد إلكتروني، هاتف، كلمة مرور قوية، أرقام، نطاقات</p>
                    <code style="font-size: 12px;">havnix install التحقق</code>
                </div>
                <div class="feature-card">
                    <div class="feature-icon"><i class="fas fa-folder-open"></i></div>
                    <h3>أدوات_الملفات</h3>
                    <p>قراءة وكتابة ملفات، JSON، CSV، سجلات، نسخ ملفات</p>
                    <code style="font-size: 12px;">havnix install أدوات_الملفات</code>
                </div>
            </div>

            <h2><i class="fas fa-folder"></i> هيكل المشروع</h2>
            <p>بعد تثبيت مكتبات، يكون هيكل مشروعك كالتالي:</p>
            <div class="code-block" style="direction: ltr; text-align: left;">
                <pre>my-project/
├── main.havnix              ← ملفك الرئيسي
├── libraries.json            ← قائمة المكتبات المثبتة
└── havnix_libraries/         ← مجلد المكتبات
    ├── التقويم_الهجري/
    │   ├── التقويم_الهجري.havnix
    │   └── package.json
    └── الألوان/
        ├── الألوان.havnix
        └── package.json</pre>
            </div>

            <h3>ملف libraries.json</h3>
            <p>يشبه <code>package.json</code> في Node.js. يتم تحديثه تلقائياً عند التثبيت والإزالة:</p>
            <div class="code-block" style="direction: ltr; text-align: left;">
                <pre>{
    "name": "مشروعي",
    "version": "1.0.0",
    "libraries": {
        "التقويم_الهجري": "1.0.0",
        "الألوان": "1.0.0"
    }
}</pre>
            </div>

            <h2><i class="fas fa-hammer"></i> إنشاء مكتبة</h2>
            <p>يمكنك إنشاء مكتبتك الخاصة ومشاركتها مع مجتمع هافنيكس.</p>

            <h3>1. هيكل المكتبة</h3>
            <div class="code-block" style="direction: ltr; text-align: left;">
                <pre>اسم_المكتبة/
├── اسم_المكتبة.havnix     ← الملف الرئيسي (يحتوي الدوال)
└── package.json             ← معلومات المكتبة</pre>
            </div>

            <h3>2. ملف package.json</h3>
            <div class="code-block" style="direction: ltr; text-align: left;">
                <pre>{
    "name": "اسم_المكتبة",
    "version": "1.0.0",
    "description": "وصف المكتبة",
    "author": "اسمك",
    "main": "اسم_المكتبة.havnix",
    "keywords": ["كلمة1", "كلمة2"],
    "license": "MIT"
}</pre>
            </div>

            <h3>3. كتابة الكود</h3>
            <p>اكتب دوال في ملف <code>.havnix</code> الرئيسي:</p>
            <div class="code-block">
                <pre><span class="cm">// مكتبة التحية</span>
<span class="cm">// الإصدار: 1.0.0</span>

<span class="kw">دالة</span> <span class="fn">حيّ</span>(<span class="var">$اسم</span>) {
    <span class="fn">قول ليهو</span>(<span class="str">"مرحبا يا "</span> <span class="op">+</span> <span class="var">$اسم</span> <span class="op">+</span> <span class="str">"!"</span>)<span class="op">;</span>
}

<span class="kw">دالة</span> <span class="fn">ودّع</span>(<span class="var">$اسم</span>) {
    <span class="fn">قول ليهو</span>(<span class="str">"مع السلامة يا "</span> <span class="op">+</span> <span class="var">$اسم</span>)<span class="op">;</span>
}</pre>
            </div>

            <h3>4. رفع المكتبة</h3>
            <p>لمشاركة مكتبتك مع المجتمع:</p>
            <ul style="padding-right: 24px; color: var(--text-light);">
                <li>اعمل Pull Request على <a href="https://github.com/Snixrs/Havnix-Language" target="_blank" style="color: var(--accent);">مستودع هافنيكس</a> وأضف مكتبتك في مجلد <code>packages/</code></li>
                <li>أو ارفعها عبر <a href="<?php echo SITE_URL; ?>/marketplace" style="color: var(--accent);">المتجر</a></li>
            </ul>

            <h2><i class="fas fa-lightbulb"></i> أمثلة استخدام</h2>

            <h3>مثال: استخدام مكتبة الرياضيات</h3>
            <div class="code-block">
                <pre><span class="kw">استورد</span> <span class="str">"havnix_libraries/الرياضيات_المتقدمة/الرياضيات_المتقدمة.havnix"</span><span class="op">;</span>

<span class="var">$أرقام</span> <span class="op">=</span> [<span class="num">10</span>, <span class="num">20</span>, <span class="num">30</span>, <span class="num">40</span>, <span class="num">50</span>]<span class="op">;</span>

<span class="fn">قول ليهو</span>(<span class="str">"المتوسط: "</span> <span class="op">+</span> <span class="fn">جيب لي</span> <span class="fn">متوسط</span>(<span class="var">$أرقام</span>))<span class="op">;</span>
<span class="fn">قول ليهو</span>(<span class="str">"5! = "</span> <span class="op">+</span> <span class="fn">جيب لي</span> <span class="fn">مضروب</span>(<span class="num">5</span>))<span class="op">;</span>
<span class="fn">قول ليهو</span>(<span class="str">"7 أولي؟ "</span> <span class="op">+</span> <span class="fn">جيب لي</span> <span class="fn">أولي</span>(<span class="num">7</span>))<span class="op">;</span>
<span class="fn">قول ليهو</span>(<span class="str">"فيبوناتشي(10) = "</span> <span class="op">+</span> <span class="fn">جيب لي</span> <span class="fn">فيبوناتشي</span>(<span class="num">10</span>))<span class="op">;</span></pre>
            </div>

            <h3>مثال: استخدام مكتبة الألوان</h3>
            <div class="code-block">
                <pre><span class="kw">استورد</span> <span class="str">"havnix_libraries/الألوان/الألوان.havnix"</span><span class="op">;</span>

<span class="fn">جيب لي</span> <span class="fn">نجاح</span>(<span class="str">"تم التثبيت بنجاح!"</span>)<span class="op">;</span>
<span class="fn">جيب لي</span> <span class="fn">تحذير</span>(<span class="str">"انتبه: الملف كبير"</span>)<span class="op">;</span>
<span class="fn">جيب لي</span> <span class="fn">خطأ_ملون</span>(<span class="str">"فشل الاتصال"</span>)<span class="op">;</span>
<span class="fn">جيب لي</span> <span class="fn">عنوان</span>(<span class="str">"برنامجي"</span>)<span class="op">;</span></pre>
            </div>
        </div>
    </div>
</div>
