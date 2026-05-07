<?php $page_title = 'مكتبات هافنيكس - Havnix Marketplace'; ?>

<section class="download-hero">
    <div class="container">
        <h1 style="font-size: 42px; margin-bottom: 16px;">مكتبات هافنيكس</h1>
        <p style="color: var(--text-light); font-size: 18px;">اكتشف مكتبات المجتمع أو شارك مكتبتك الخاصة</p>
    </div>
</section>

<section style="padding: 0 0 60px; background: var(--bg-dark);">
    <div class="container">
        <!-- Search & Filter -->
        <div style="display: flex; gap: 16px; margin-bottom: 32px; flex-wrap: wrap;">
            <input type="text" id="pkg-search" placeholder="ابحث عن مكتبة..." style="flex: 1; min-width: 200px; padding: 12px 16px; background: var(--surface); border: 1px solid var(--border); border-radius: 8px; color: white; font-size: 15px; direction: rtl;">
            <select id="pkg-filter" style="padding: 12px 16px; background: var(--surface); border: 1px solid var(--border); border-radius: 8px; color: white; font-size: 15px;">
                <option value="">كل الفئات</option>
                <option value="utils">أدوات</option>
                <option value="math">رياضيات</option>
                <option value="text">نصوص</option>
                <option value="ui">واجهات</option>
                <option value="data">بيانات</option>
                <option value="network">شبكات</option>
            </select>
        </div>

        <!-- Package Grid -->
        <div class="packages-grid">
            <div class="package-card" data-category="utils">
                <div class="pkg-header">
                    <span class="pkg-name"><i class="fas fa-chart-bar" style="color: var(--accent);"></i> رسوم_بيانية</span>
                    <span class="pkg-version">v1.0.0</span>
                </div>
                <p class="pkg-desc">مكتبة لرسم الأشكال البيانية والمخططات. ارسم أعمدة ودوائر وخطوط بسهولة.</p>
                <div class="pkg-meta">
                    <span><i class="fas fa-user"></i> أحمد</span>
                    <span><i class="fas fa-download"></i> 245</span>
                    <span><i class="fas fa-star" style="color: #f59e0b;"></i> 4.5</span>
                    <span class="pkg-status approved"><i class="fas fa-check-circle"></i> مُعتمد</span>
                </div>
            </div>

            <div class="package-card" data-category="utils">
                <div class="pkg-header">
                    <span class="pkg-name"><i class="fas fa-lock" style="color: var(--accent);"></i> تشفير</span>
                    <span class="pkg-version">v2.1.0</span>
                </div>
                <p class="pkg-desc">أدوات تشفير وفك تشفير النصوص. دعم Base64 وMD5 وSHA256.</p>
                <div class="pkg-meta">
                    <span><i class="fas fa-user"></i> محمد</span>
                    <span><i class="fas fa-download"></i> 189</span>
                    <span><i class="fas fa-star" style="color: #f59e0b;"></i> 4.8</span>
                    <span class="pkg-status approved"><i class="fas fa-check-circle"></i> مُعتمد</span>
                </div>
            </div>

            <div class="package-card" data-category="utils">
                <div class="pkg-header">
                    <span class="pkg-name"><i class="fas fa-calendar-alt" style="color: var(--accent);"></i> تاريخ_هجري</span>
                    <span class="pkg-version">v1.2.0</span>
                </div>
                <p class="pkg-desc">تحويل بين التاريخ الهجري والميلادي. حساب الأيام والأشهر.</p>
                <div class="pkg-meta">
                    <span><i class="fas fa-user"></i> علي</span>
                    <span><i class="fas fa-download"></i> 320</span>
                    <span><i class="fas fa-star" style="color: #f59e0b;"></i> 4.9</span>
                    <span class="pkg-status approved"><i class="fas fa-check-circle"></i> مُعتمد</span>
                </div>
            </div>

            <div class="package-card" data-category="network">
                <div class="pkg-header">
                    <span class="pkg-name"><i class="fas fa-language" style="color: var(--accent);"></i> ترجمة</span>
                    <span class="pkg-version">v0.5.0</span>
                </div>
                <p class="pkg-desc">مكتبة ترجمة النصوص بين اللغات باستخدام APIs مجانية.</p>
                <div class="pkg-meta">
                    <span><i class="fas fa-user"></i> خالد</span>
                    <span><i class="fas fa-download"></i> 98</span>
                    <span><i class="fas fa-star" style="color: #f59e0b;"></i> 4.2</span>
                    <span class="pkg-status pending"><i class="fas fa-clock"></i> قيد المراجعة</span>
                </div>
            </div>

            <div class="package-card" data-category="ui">
                <div class="pkg-header">
                    <span class="pkg-name"><i class="fas fa-gamepad" style="color: var(--accent);"></i> العاب</span>
                    <span class="pkg-version">v1.0.0</span>
                </div>
                <p class="pkg-desc">أدوات بناء ألعاب بسيطة. رسم أشكال وتحريكها والتفاعل مع المستخدم.</p>
                <div class="pkg-meta">
                    <span><i class="fas fa-user"></i> عمر</span>
                    <span><i class="fas fa-download"></i> 156</span>
                    <span><i class="fas fa-star" style="color: #f59e0b;"></i> 4.6</span>
                    <span class="pkg-status approved"><i class="fas fa-check-circle"></i> مُعتمد</span>
                </div>
            </div>

            <div class="package-card" data-category="network">
                <div class="pkg-header">
                    <span class="pkg-name"><i class="fas fa-envelope" style="color: var(--accent);"></i> بريد</span>
                    <span class="pkg-version">v1.1.0</span>
                </div>
                <p class="pkg-desc">إرسال بريد إلكتروني عبر SMTP. يدعم HTML والمرفقات.</p>
                <div class="pkg-meta">
                    <span><i class="fas fa-user"></i> فاطمة</span>
                    <span><i class="fas fa-download"></i> 134</span>
                    <span><i class="fas fa-star" style="color: #f59e0b;"></i> 4.4</span>
                    <span class="pkg-status approved"><i class="fas fa-check-circle"></i> مُعتمد</span>
                </div>
            </div>
        </div>

        <!-- Upload Form -->
        <div style="margin-top: 48px; background: var(--surface); border-radius: 16px; padding: 32px; border: 1px solid var(--border);">
            <div style="text-align: center; margin-bottom: 24px;">
                <i class="fas fa-box-open" style="font-size: 48px; color: var(--accent); margin-bottom: 16px; display: block;"></i>
                <h3>شارك مكتبتك مع المجتمع</h3>
                <p style="color: var(--text-muted);">ارفع مكتبتك وبعد الموافقة عليها هتكون متاحة للجميع</p>
            </div>

            <form id="upload-form" style="max-width: 500px; margin: 0 auto; display: flex; flex-direction: column; gap: 16px;">
                <div>
                    <label style="display: block; margin-bottom: 6px; color: var(--text-light); font-size: 14px;">اسم المكتبة</label>
                    <input name="name" type="text" placeholder="مثال: أدوات_رياضية" style="width: 100%; padding: 10px 14px; background: var(--bg-dark); border: 1px solid var(--border); border-radius: 8px; color: white; font-size: 14px; direction: rtl;">
                </div>
                <div>
                    <label style="display: block; margin-bottom: 6px; color: var(--text-light); font-size: 14px;">الوصف</label>
                    <textarea name="description" rows="3" placeholder="اشرح شنو المكتبة بتسوي..." style="width: 100%; padding: 10px 14px; background: var(--bg-dark); border: 1px solid var(--border); border-radius: 8px; color: white; font-size: 14px; resize: vertical; direction: rtl;"></textarea>
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                    <div>
                        <label style="display: block; margin-bottom: 6px; color: var(--text-light); font-size: 14px;">الفئة</label>
                        <select name="category" style="width: 100%; padding: 10px 14px; background: var(--bg-dark); border: 1px solid var(--border); border-radius: 8px; color: white; font-size: 14px;">
                            <option value="utils">أدوات</option>
                            <option value="math">رياضيات</option>
                            <option value="text">نصوص</option>
                            <option value="ui">واجهات</option>
                            <option value="data">بيانات</option>
                            <option value="network">شبكات</option>
                        </select>
                    </div>
                    <div>
                        <label style="display: block; margin-bottom: 6px; color: var(--text-light); font-size: 14px;">الإصدار</label>
                        <input name="version" type="text" value="1.0.0" style="width: 100%; padding: 10px 14px; background: var(--bg-dark); border: 1px solid var(--border); border-radius: 8px; color: white; font-size: 14px;">
                    </div>
                </div>
                <div>
                    <label style="display: block; margin-bottom: 6px; color: var(--text-light); font-size: 14px;">ملف المكتبة (.havnix أو .zip)</label>
                    <input name="package_file" type="file" accept=".havnix,.zip,.tar.gz" style="width: 100%; padding: 10px 14px; background: var(--bg-dark); border: 1px solid var(--border); border-radius: 8px; color: white; font-size: 14px;">
                </div>
                <button type="submit" class="btn btn-primary" style="width: 100%;"><i class="fas fa-upload"></i> رفع المكتبة للمراجعة</button>
                <p style="text-align: center; font-size: 12px; color: var(--text-muted);">سيتم مراجعة المكتبة من قبل فريق هافنيكس قبل نشرها</p>
            </form>
        </div>

        <!-- How to use -->
        <div class="install-steps" style="margin-top: 48px;">
            <h2 style="color: var(--accent);"><i class="fas fa-book"></i> كيف تستخدم المكتبات</h2>

            <div class="step">
                <div class="step-num">1</div>
                <div class="step-content">
                    <h4>حمّل المكتبة</h4>
                    <p style="color: var(--text-muted);">اضغط تحميل على صفحة المكتبة</p>
                </div>
            </div>

            <div class="step">
                <div class="step-num">2</div>
                <div class="step-content">
                    <h4>ضع الملف في مجلد مشروعك</h4>
                    <div class="code-block" style="margin: 8px 0; direction: ltr; text-align: left;">
                        <pre>project/
├── main.havnix
└── libs/
    └── رسوم_بيانية.havnix</pre>
                    </div>
                </div>
            </div>

            <div class="step">
                <div class="step-num">3</div>
                <div class="step-content">
                    <h4>استوردها في كودك</h4>
                    <div class="code-block" style="margin: 8px 0; direction: ltr; text-align: left;">
                        <pre>استورد "libs/رسوم_بيانية.havnix";</pre>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
