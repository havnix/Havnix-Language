<?php $page_title = 'توثيق هافنيكس - Havnix Docs'; ?>

<div class="container">
    <div class="docs-layout">
        <?php include INCLUDES_PATH . '/docs-sidebar.php'; ?>

        <div class="docs-content">
            <h1>توثيق لغة هافنيكس</h1>
            <p>مرحباً بك في التوثيق الرسمي للغة هافنيكس - لغة برمجة كاملة بالعربية السودانية.</p>

            <h2>ما هي هافنيكس؟</h2>
            <p>هافنيكس هي لغة برمجة عربية مكتوبة بالسودانية، مصممة لتسهيل البرمجة على المتحدثين بالعربية. تدعم اللغة المتغيرات، الشروط، الحلقات، الدوال، معالجة الأخطاء، قواعد البيانات، APIs، وتطبيقات سطح المكتب.</p>

            <h2>البداية السريعة</h2>

            <h3>1. التثبيت</h3>
            <div class="code-block" style="direction: ltr; text-align: left;">
                <pre>git clone https://github.com/Snixrs/Havnix-Language.git
cd Havnix-Language
python3 ide.py</pre>
            </div>

            <h3>2. أول برنامج</h3>
            <p>أنشئ ملف <code>hello.havnix</code> واكتب:</p>
            <div class="code-block">
                <pre><span class="fn">قول ليهو</span>(<span class="str">"مرحبا يا عالم!"</span>)<span class="op">;</span></pre>
            </div>

            <h3>3. التشغيل</h3>
            <div class="code-block" style="direction: ltr; text-align: left;">
                <pre>python3 havnix.py hello.havnix</pre>
            </div>
            <p>أو استخدم IDE واضغط <code>F5</code></p>

            <h2>أقسام التوثيق</h2>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin-top: 24px;">
                <a href="<?php echo SITE_URL; ?>/docs/start" class="feature-card" style="text-decoration: none;">
                    <div class="feature-icon">🚀</div>
                    <h3>البداية السريعة</h3>
                    <p>تعلم الأساسيات: متغيرات، شروط، حلقات، دوال</p>
                </a>

                <a href="<?php echo SITE_URL; ?>/docs/syntax" class="feature-card" style="text-decoration: none;">
                    <div class="feature-icon">📐</div>
                    <h3>بنية اللغة</h3>
                    <p>تفاصيل القواعد النحوية وأنواع البيانات والعمليات</p>
                </a>

                <a href="<?php echo SITE_URL; ?>/docs/functions" class="feature-card" style="text-decoration: none;">
                    <div class="feature-icon">⚡</div>
                    <h3>الدوال المدمجة</h3>
                    <p>30+ دالة جاهزة للنصوص والرياضيات والملفات</p>
                </a>

                <a href="<?php echo SITE_URL; ?>/docs/advanced" class="feature-card" style="text-decoration: none;">
                    <div class="feature-icon">🔥</div>
                    <h3>الميزات المتقدمة</h3>
                    <p>MySQL، APIs، واجهات سطح المكتب</p>
                </a>
            </div>
        </div>
    </div>
</div>
