<?php $page_title = 'مساعدة - Havnix Help'; ?>

<section class="download-hero">
    <div class="container">
        <h1 style="font-size: 42px; margin-bottom: 16px;">مركز المساعدة</h1>
        <p style="color: var(--text-light); font-size: 18px;">إجابات للأسئلة الشائعة ومعلومات مفيدة</p>
    </div>
</section>

<section style="padding: 60px 0; background: var(--bg-dark);">
    <div class="container" style="max-width: 900px;">

        <!-- FAQ -->
        <h2 style="color: var(--accent); margin-bottom: 32px; text-align: center;"><i class="fas fa-circle-question"></i> الأسئلة الشائعة</h2>

        <div class="faq-list">
            <div class="faq-item">
                <button class="faq-question" onclick="this.parentElement.classList.toggle('open')">
                    <span><i class="fas fa-question-circle" style="color: var(--accent);"></i> شنو هي هافنيكس؟</span>
                    <i class="fas fa-chevron-down faq-arrow"></i>
                </button>
                <div class="faq-answer">
                    <p>هافنيكس هي لغة برمجة كاملة مكتوبة بالعربي السوداني. كل الأوامر والكلمات المفتاحية بالعربي، وبتدعم المتغيرات، الشروط، الحلقات، الدوال، معالجة الأخطاء، قواعد البيانات MySQL، التعامل مع APIs، وتصميم تطبيقات سطح مكتب بواجهات رسومية.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question" onclick="this.parentElement.classList.toggle('open')">
                    <span><i class="fas fa-laptop" style="color: var(--accent);"></i> هافنيكس بتشتغل على أي نظام تشغيل؟</span>
                    <i class="fas fa-chevron-down faq-arrow"></i>
                </button>
                <div class="faq-answer">
                    <p>هافنيكس بتشتغل على Windows و Linux و macOS. المتطلب الوحيد هو تثبيت Python 3.8 أو أعلى.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question" onclick="this.parentElement.classList.toggle('open')">
                    <span><i class="fas fa-download" style="color: var(--accent);"></i> كيف أثبّت هافنيكس؟</span>
                    <i class="fas fa-chevron-down faq-arrow"></i>
                </button>
                <div class="faq-answer">
                    <p>عندك طريقتين:</p>
                    <ul style="padding-right: 20px; margin: 8px 0;">
                        <li style="margin: 8px 0;">حمّل المثبّت الجاهز من <a href="<?php echo SITE_URL; ?>/download" style="color: var(--accent);">صفحة التحميل</a></li>
                        <li style="margin: 8px 0;">أو ثبّت يدوياً:
                            <div class="code-block" style="margin: 8px 0; direction: ltr; text-align: left;">
                                <pre>git clone https://github.com/Snixrs/Havnix-Language.git
cd Havnix-Language
pip install -r requirements.txt
python3 ide.py</pre>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question" onclick="this.parentElement.classList.toggle('open')">
                    <span><i class="fas fa-play" style="color: var(--accent);"></i> كيف أشغّل برنامج هافنيكس؟</span>
                    <i class="fas fa-chevron-down faq-arrow"></i>
                </button>
                <div class="faq-answer">
                    <p>عندك طريقتين:</p>
                    <ul style="padding-right: 20px; margin: 8px 0;">
                        <li style="margin: 8px 0;">من IDE: افتح الملف واضغط <code>F5</code></li>
                        <li style="margin: 8px 0;">من سطر الأوامر:
                            <div class="code-block" style="margin: 8px 0; direction: ltr; text-align: left;">
                                <pre>python3 havnix.py filename.havnix</pre>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question" onclick="this.parentElement.classList.toggle('open')">
                    <span><i class="fas fa-code" style="color: var(--accent);"></i> هل لازم أعرف إنجليزي عشان أستخدم هافنيكس؟</span>
                    <i class="fas fa-chevron-down faq-arrow"></i>
                </button>
                <div class="faq-answer">
                    <p>لا! هافنيكس مصممة بالكامل بالعربي السوداني. كل الأوامر والكلمات المفتاحية بالعربي. بس بتحتاج تعرف حروف لاتينية بسيطة في أسماء المتغيرات لو حبيت (وممكن تستخدم أسماء عربية).</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question" onclick="this.parentElement.classList.toggle('open')">
                    <span><i class="fas fa-database" style="color: var(--accent);"></i> كيف أتصل بقاعدة بيانات MySQL؟</span>
                    <i class="fas fa-chevron-down faq-arrow"></i>
                </button>
                <div class="faq-answer">
                    <div class="code-block" style="direction: ltr; text-align: left;">
                        <pre>$قاعدة = اتصل_قاعدة("localhost", "root", "password", "my_db");
$نتائج = استعلم($قاعدة, "SELECT * FROM users");
لكل $صف في $نتائج {
    قول ليهو($صف);
}
اقفل_قاعدة($قاعدة);</pre>
                    </div>
                    <p style="margin-top: 8px;">لازم يكون MySQL مثبت ومشتغل على جهازك.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question" onclick="this.parentElement.classList.toggle('open')">
                    <span><i class="fas fa-globe" style="color: var(--accent);"></i> كيف أجيب بيانات من API؟</span>
                    <i class="fas fa-chevron-down faq-arrow"></i>
                </button>
                <div class="faq-answer">
                    <div class="code-block" style="direction: ltr; text-align: left;">
                        <pre>$رد = جيب_من("https://api.example.com/data");
قول ليهو($رد);

// POST request
$بيانات = {"الاسم": "عثمان"};
$رد = رسل_لي("https://api.example.com/users", $بيانات);</pre>
                    </div>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question" onclick="this.parentElement.classList.toggle('open')">
                    <span><i class="fas fa-desktop" style="color: var(--accent);"></i> كيف أصمم تطبيق سطح مكتب؟</span>
                    <i class="fas fa-chevron-down faq-arrow"></i>
                </button>
                <div class="faq-answer">
                    <div class="code-block" style="direction: ltr; text-align: left;">
                        <pre>$نافذة = نافذة_جديدة("تطبيقي", 400, 300);
نص_ثابت($نافذة, "مرحبا بك!");
زر($نافذة, "اضغط هنا", "on_click");

دالة on_click() {
    قول ليهو("تم الضغط!");
}

شغل_واجهة($نافذة);</pre>
                    </div>
                    <p style="margin-top: 8px;">يحتاج مكتبة <code>tkinter</code> (متوفرة افتراضياً في Python).</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question" onclick="this.parentElement.classList.toggle('open')">
                    <span><i class="fas fa-cubes" style="color: var(--accent);"></i> كيف أستخدم مكتبات خارجية؟</span>
                    <i class="fas fa-chevron-down faq-arrow"></i>
                </button>
                <div class="faq-answer">
                    <p>حمّل المكتبة من <a href="<?php echo SITE_URL; ?>/marketplace" style="color: var(--accent);">المتجر</a> وضعها في مجلد مشروعك:</p>
                    <div class="code-block" style="margin: 8px 0; direction: ltr; text-align: left;">
                        <pre>استورد "libs/رسوم_بيانية.havnix";</pre>
                    </div>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question" onclick="this.parentElement.classList.toggle('open')">
                    <span><i class="fas fa-file-export" style="color: var(--accent);"></i> كيف أحوّل برنامجي لملف EXE؟</span>
                    <i class="fas fa-chevron-down faq-arrow"></i>
                </button>
                <div class="faq-answer">
                    <div class="code-block" style="direction: ltr; text-align: left;">
                        <pre>pip install pyinstaller
python3 build_exe.py</pre>
                    </div>
                    <p style="margin-top: 8px;">الملف التنفيذي هيكون في مجلد <code>dist/</code></p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question" onclick="this.parentElement.classList.toggle('open')">
                    <span><i class="fab fa-osi" style="color: var(--accent);"></i> هل هافنيكس مجانية؟</span>
                    <i class="fas fa-chevron-down faq-arrow"></i>
                </button>
                <div class="faq-answer">
                    <p>نعم! هافنيكس مفتوحة المصدر بالكامل تحت رخصة MIT. يعني ممكن تستخدمها وتعدل عليها وتوزعها بحرية كاملة.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question" onclick="this.parentElement.classList.toggle('open')">
                    <span><i class="fas fa-hands-helping" style="color: var(--accent);"></i> كيف أساهم في تطوير هافنيكس؟</span>
                    <i class="fas fa-chevron-down faq-arrow"></i>
                </button>
                <div class="faq-answer">
                    <ul style="padding-right: 20px;">
                        <li style="margin: 8px 0;"><i class="fas fa-bug"></i> أبلغ عن مشاكل على <a href="https://github.com/Snixrs/Havnix-Language/issues" target="_blank" style="color: var(--accent);">GitHub Issues</a></li>
                        <li style="margin: 8px 0;"><i class="fas fa-code-merge"></i> اعمل Pull Request بتحسينات</li>
                        <li style="margin: 8px 0;"><i class="fas fa-cubes"></i> ارفع مكتبات على <a href="<?php echo SITE_URL; ?>/marketplace" style="color: var(--accent);">المتجر</a></li>
                        <li style="margin: 8px 0;"><i class="fas fa-share-alt"></i> شارك المشروع مع أصحابك</li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- Contact -->
        <div style="margin-top: 60px; text-align: center; background: var(--surface); border-radius: 16px; padding: 40px; border: 1px solid var(--border);">
            <i class="fas fa-headset" style="font-size: 40px; color: var(--accent); margin-bottom: 16px;"></i>
            <h2 style="margin-bottom: 12px;">لسه عندك سؤال؟</h2>
            <p style="color: var(--text-muted); margin-bottom: 24px;">تواصل معانا أو اطرح سؤالك على GitHub</p>
            <div style="display: flex; gap: 12px; justify-content: center; flex-wrap: wrap;">
                <a href="https://github.com/Snixrs/Havnix-Language/issues/new" target="_blank" class="btn btn-primary"><i class="fas fa-plus-circle"></i> اطرح سؤال</a>
                <a href="https://github.com/Snixrs/Havnix-Language/discussions" target="_blank" class="btn btn-outline"><i class="fas fa-comments"></i> المنتدى</a>
            </div>
        </div>
    </div>
</section>
