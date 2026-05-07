<?php $page_title = 'Havnix - لغة برمجة عربية سودانية'; ?>

<!-- Hero -->
<section class="hero">
    <div class="hero-content">
        <span class="hero-badge"><span class="fi fi-sd"></span> الإصدار <?php echo SITE_VERSION; ?> متاح الآن</span>
        <h1>برمج بالسودانية مع هافنيكس</h1>
        <p>لغة برمجة كاملة بالعربية السودانية. اكتب كود بلغتك الأم، ابني تطبيقات سطح مكتب، اتصل بقواعد بيانات، وتعامل مع APIs.</p>

        <div class="hero-buttons">
            <a href="<?php echo SITE_URL; ?>/download" class="btn btn-primary"><i class="fas fa-download"></i> حمّل الآن</a>
            <a href="<?php echo SITE_URL; ?>/docs/start" class="btn btn-outline"><i class="fas fa-book-open"></i> ابدأ التعلم</a>
        </div>

        <div class="hero-code">
            <pre><span class="cm">// مرحبا بك في هافنيكس!</span>
<span class="var">$الاسم</span> <span class="op">=</span> <span class="str">"عثمان"</span><span class="op">;</span>
<span class="var">$العمر</span> <span class="op">=</span> <span class="num">20</span><span class="op">;</span>

<span class="fn">قول ليهو</span>(<span class="str">"مرحبا يا <span class="var">$الاسم</span>!"</span>)<span class="op">;</span>

<span class="kw">لو</span> (<span class="var">$العمر</span> <span class="op">>=</span> <span class="num">18</span>) {
    <span class="fn">قول ليهو</span>(<span class="str">"انت كبير!"</span>)<span class="op">;</span>
}</pre>
        </div>
    </div>
</section>

<!-- Stats -->
<section style="padding: 40px 0; background: var(--surface); border-bottom: 1px solid var(--border);">
    <div class="container">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 24px; text-align: center;">
            <div>
                <div style="font-size: 36px; font-weight: 800; color: var(--accent);">30+</div>
                <div style="color: var(--text-muted); font-size: 14px;">دالة مدمجة</div>
            </div>
            <div>
                <div style="font-size: 36px; font-weight: 800; color: var(--accent);">15+</div>
                <div style="color: var(--text-muted); font-size: 14px;">كلمة مفتاحية</div>
            </div>
            <div>
                <div style="font-size: 36px; font-weight: 800; color: var(--accent);">12+</div>
                <div style="color: var(--text-muted); font-size: 14px;">مثال جاهز</div>
            </div>
            <div>
                <div style="font-size: 36px; font-weight: 800; color: var(--accent);">3</div>
                <div style="color: var(--text-muted); font-size: 14px;">أنظمة تشغيل مدعومة</div>
            </div>
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
                <div class="feature-icon"><i class="fas fa-desktop"></i></div>
                <h3>تطبيقات سطح مكتب</h3>
                <p>صمم واجهات رسومية كاملة بأزرار ونصوص ومدخلات وقوائم منسدلة - كل شي بالعربي.</p>
            </div>

            <div class="feature-card">
                <div class="feature-icon"><i class="fas fa-database"></i></div>
                <h3>قواعد بيانات MySQL</h3>
                <p>اتصل بقواعد البيانات، نفذ استعلامات، واعمل عمليات CRUD كاملة بأوامر عربية.</p>
            </div>

            <div class="feature-card">
                <div class="feature-icon"><i class="fas fa-globe"></i></div>
                <h3>تعامل مع APIs</h3>
                <p>ارسل طلبات GET, POST, PUT, DELETE لأي API. اجلب بيانات من الإنترنت بسهولة.</p>
            </div>

            <div class="feature-card">
                <div class="feature-icon"><i class="fas fa-code"></i></div>
                <h3>IDE متكامل</h3>
                <p>بيئة تطوير مدمجة مع تلوين الكود، مستكشف ملفات، طرفية تفاعلية، ودعم Git.</p>
            </div>

            <div class="feature-card">
                <div class="feature-icon"><i class="fas fa-cubes"></i></div>
                <h3>مكتبات مجتمعية</h3>
                <p>استخدم مكتبات جاهزة من المجتمع أو ارفع مكتبتك الخاصة ليستفيد منها الآخرون.</p>
            </div>

            <div class="feature-card">
                <div class="feature-icon"><i class="fas fa-wrench"></i></div>
                <h3>30+ دالة مدمجة</h3>
                <p>نصوص، رياضيات، ملفات، JSON، تواريخ - كل الأدوات اللي بتحتاجها موجودة.</p>
            </div>
        </div>
    </div>
</section>

<!-- Why Havnix -->
<section style="padding: 80px 0; background: var(--bg-dark);">
    <div class="container">
        <h2 class="section-title">ليه هافنيكس؟</h2>
        <p class="section-subtitle">لغة مصممة خصيصاً لتسهيل البرمجة على العرب</p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 32px; margin-top: 40px;">
            <div style="display: flex; gap: 16px; align-items: flex-start;">
                <div style="background: var(--primary); width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                    <i class="fas fa-language" style="color: white; font-size: 20px;"></i>
                </div>
                <div>
                    <h3 style="margin-bottom: 8px;">بدون حاجز اللغة</h3>
                    <p style="color: var(--text-muted); font-size: 14px;">كل الأوامر بالعربي السوداني. ما محتاج تتعلم إنجليزي عشان تبرمج.</p>
                </div>
            </div>

            <div style="display: flex; gap: 16px; align-items: flex-start;">
                <div style="background: var(--primary); width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                    <i class="fas fa-graduation-cap" style="color: white; font-size: 20px;"></i>
                </div>
                <div>
                    <h3 style="margin-bottom: 8px;">سهلة التعلم</h3>
                    <p style="color: var(--text-muted); font-size: 14px;">بنية بسيطة ومباشرة. مثالية للمبتدئين والطلاب اللي عايزين يتعلمو البرمجة.</p>
                </div>
            </div>

            <div style="display: flex; gap: 16px; align-items: flex-start;">
                <div style="background: var(--primary); width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                    <i class="fas fa-shield-halved" style="color: white; font-size: 20px;"></i>
                </div>
                <div>
                    <h3 style="margin-bottom: 8px;">آمنة ومستقرة</h3>
                    <p style="color: var(--text-muted); font-size: 14px;">مبنية على Python مع معالجة أخطاء متقدمة. كودك بشتغل بأمان.</p>
                </div>
            </div>

            <div style="display: flex; gap: 16px; align-items: flex-start;">
                <div style="background: var(--primary); width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                    <i class="fab fa-osi" style="color: white; font-size: 20px;"></i>
                </div>
                <div>
                    <h3 style="margin-bottom: 8px;">مفتوحة المصدر</h3>
                    <p style="color: var(--text-muted); font-size: 14px;">مجانية بالكامل تحت رخصة MIT. ساهم في التطوير وكن جزء من المجتمع.</p>
                </div>
            </div>

            <div style="display: flex; gap: 16px; align-items: flex-start;">
                <div style="background: var(--primary); width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                    <i class="fas fa-laptop-code" style="color: white; font-size: 20px;"></i>
                </div>
                <div>
                    <h3 style="margin-bottom: 8px;">تعمل في كل مكان</h3>
                    <p style="color: var(--text-muted); font-size: 14px;">Windows, Linux, macOS - حمّل وشغّل على أي نظام.</p>
                </div>
            </div>

            <div style="display: flex; gap: 16px; align-items: flex-start;">
                <div style="background: var(--primary); width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                    <i class="fas fa-puzzle-piece" style="color: white; font-size: 20px;"></i>
                </div>
                <div>
                    <h3 style="margin-bottom: 8px;">قابلة للتوسعة</h3>
                    <p style="color: var(--text-muted); font-size: 14px;">نظام مكتبات يمكنك تثبيتها واستخدامها بأمر <code>استورد</code>.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Quick Examples -->
<section style="padding: 80px 0; background: var(--surface);">
    <div class="container">
        <h2 class="section-title">شوف كيف سهل</h2>
        <p class="section-subtitle">كل أمر بالعربي. ما في داعي تتعلم إنجليزي عشان تبرمج.</p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 24px;">
            <div>
                <h3 style="margin-bottom: 12px; color: var(--accent);"><i class="fas fa-list"></i> قوائم وحلقات</h3>
                <div class="code-block">
                    <pre><span class="var">$فواكه</span> <span class="op">=</span> [<span class="str">"تفاح"</span><span class="op">,</span> <span class="str">"موز"</span><span class="op">,</span> <span class="str">"برتقال"</span>]<span class="op">;</span>
<span class="kw">لكل</span> <span class="var">$فاكهة</span> <span class="kw">في</span> <span class="var">$فواكه</span> {
    <span class="fn">قول ليهو</span>(<span class="var">$فاكهة</span>)<span class="op">;</span>
}</pre>
                </div>
            </div>

            <div>
                <h3 style="margin-bottom: 12px; color: var(--accent);"><i class="fas fa-bolt"></i> دوال</h3>
                <div class="code-block">
                    <pre><span class="kw">دالة</span> <span class="fn">جمع</span>(أ<span class="op">,</span> ب) {
    <span class="kw">ارجع</span> أ <span class="op">+</span> ب<span class="op">;</span>
}
<span class="var">$النتيجة</span> <span class="op">=</span> <span class="fn">جيب لي</span> <span class="fn">جمع</span>(<span class="num">5</span><span class="op">,</span> <span class="num">3</span>)<span class="op">;</span>
<span class="fn">قول ليهو</span>(<span class="var">$النتيجة</span>)<span class="op">;</span>  <span class="cm">// 8</span></pre>
                </div>
            </div>

            <div>
                <h3 style="margin-bottom: 12px; color: var(--accent);"><i class="fas fa-database"></i> قاعدة بيانات</h3>
                <div class="code-block">
                    <pre><span class="var">$قاعدة</span> <span class="op">=</span> <span class="fn">اتصل_قاعدة</span>(<span class="str">"localhost"</span><span class="op">,</span> <span class="str">"root"</span><span class="op">,</span> <span class="str">"pass"</span><span class="op">,</span> <span class="str">"db"</span>)<span class="op">;</span>
<span class="var">$نتائج</span> <span class="op">=</span> <span class="fn">استعلم</span>(<span class="var">$قاعدة</span><span class="op">,</span> <span class="str">"SELECT * FROM users"</span>)<span class="op">;</span>
<span class="kw">لكل</span> <span class="var">$صف</span> <span class="kw">في</span> <span class="var">$نتائج</span> {
    <span class="fn">قول ليهو</span>(<span class="var">$صف</span>)<span class="op">;</span>
}</pre>
                </div>
            </div>

            <div>
                <h3 style="margin-bottom: 12px; color: var(--accent);"><i class="fas fa-globe"></i> APIs</h3>
                <div class="code-block">
                    <pre><span class="var">$رد</span> <span class="op">=</span> <span class="fn">جيب_من</span>(<span class="str">"https://api.example.com/data"</span>)<span class="op">;</span>
<span class="fn">اطبع</span>(<span class="var">$رد</span>)<span class="op">;</span>

<span class="var">$بيانات</span> <span class="op">=</span> {<span class="str">"الاسم"</span><span class="op">:</span> <span class="str">"عثمان"</span>}<span class="op">;</span>
<span class="var">$رد</span> <span class="op">=</span> <span class="fn">رسل_لي</span>(<span class="str">"https://api.example.com"</span><span class="op">,</span> <span class="var">$بيانات</span>)<span class="op">;</span></pre>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Developer -->
<section style="padding: 80px 0; background: var(--bg-dark);">
    <div class="container">
        <div style="display: flex; align-items: center; gap: 40px; max-width: 800px; margin: 0 auto; flex-wrap: wrap; justify-content: center;">
            <div style="width: 120px; height: 120px; border-radius: 50%; background: linear-gradient(135deg, #1B569A, #60a5fa); display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                <i class="fas fa-user" style="font-size: 48px; color: white;"></i>
            </div>
            <div style="flex: 1; min-width: 250px;">
                <h2 style="margin-bottom: 8px;">المطور</h2>
                <h3 style="color: var(--accent); font-size: 24px; margin-bottom: 8px;">Osman Salih <span style="color: var(--text-muted); font-size: 16px;">(Snixrs)</span></h3>
                <p style="color: var(--text-muted); margin-bottom: 12px;">مطور سوداني، عمر 20 سنة. صمم وبرمج لغة هافنيكس لتمكين العرب من البرمجة بلغتهم الأم.</p>
                <div style="display: flex; gap: 12px; align-items: center;">
                    <a href="https://github.com/Snixrs" target="_blank" class="btn btn-outline" style="padding: 8px 16px; font-size: 14px;"><i class="fab fa-github"></i> GitHub</a>
                    <span class="fi fi-sd" style="font-size: 20px;"></span>
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
            <a href="<?php echo SITE_URL; ?>/download" class="btn btn-primary"><i class="fas fa-download"></i> حمّل مجاناً</a>
            <a href="https://github.com/Snixrs/Havnix-Language" target="_blank" class="btn btn-outline"><i class="fab fa-github"></i> GitHub</a>
        </div>
    </div>
</section>
