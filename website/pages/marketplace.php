<?php $page_title = 'مكتبات هافنيكس - Havnix Marketplace'; ?>

<section class="marketplace-header">
    <div class="container">
        <h1 style="font-size: 42px; margin-bottom: 16px;">مكتبات هافنيكس</h1>
        <p style="color: var(--text-light); font-size: 18px;">اكتشف مكتبات المجتمع أو شارك مكتبتك الخاصة</p>
    </div>
</section>

<section style="padding: 0 0 60px; background: var(--bg-dark);">
    <div class="container">

        <!-- Search & Filter -->
        <div style="display: flex; gap: 12px; margin-bottom: 32px; flex-wrap: wrap;">
            <input type="text" id="search-packages" placeholder="🔍 ابحث عن مكتبة..."
                   style="flex: 1; min-width: 250px; padding: 12px 16px; border-radius: 8px; border: 1px solid var(--border); background: var(--surface); color: white; font-size: 15px; font-family: inherit;">
            <select id="filter-category"
                    style="padding: 12px 16px; border-radius: 8px; border: 1px solid var(--border); background: var(--surface); color: white; font-size: 15px;">
                <option value="">كل الفئات</option>
                <option value="utils">أدوات</option>
                <option value="math">رياضيات</option>
                <option value="text">نصوص</option>
                <option value="ui">واجهات</option>
                <option value="data">بيانات</option>
                <option value="network">شبكات</option>
            </select>
        </div>

        <!-- Packages Grid -->
        <div class="marketplace-grid" id="packages-grid">

            <!-- Example packages (in production, loaded from MySQL) -->
            <div class="package-card">
                <div class="package-header">
                    <span class="package-name">📊 رسوم_بيانية</span>
                    <span class="package-version">v1.0.0</span>
                </div>
                <p class="package-desc">مكتبة لرسم الأشكال البيانية والمخططات. ارسم أعمدة ودوائر وخطوط بسهولة.</p>
                <div class="package-meta">
                    <span>👤 أحمد</span>
                    <span>⬇ 245</span>
                    <span>⭐ 4.5</span>
                    <span class="package-status status-approved">مُعتمد</span>
                </div>
            </div>

            <div class="package-card">
                <div class="package-header">
                    <span class="package-name">🔐 تشفير</span>
                    <span class="package-version">v2.1.0</span>
                </div>
                <p class="package-desc">أدوات تشفير وفك تشفير النصوص. دعم Base64 وMD5 وSHA256.</p>
                <div class="package-meta">
                    <span>👤 محمد</span>
                    <span>⬇ 189</span>
                    <span>⭐ 4.8</span>
                    <span class="package-status status-approved">مُعتمد</span>
                </div>
            </div>

            <div class="package-card">
                <div class="package-header">
                    <span class="package-name">📅 تاريخ_هجري</span>
                    <span class="package-version">v1.2.0</span>
                </div>
                <p class="package-desc">تحويل بين التاريخ الهجري والميلادي. حساب الأيام والأشهر.</p>
                <div class="package-meta">
                    <span>👤 علي</span>
                    <span>⬇ 320</span>
                    <span>⭐ 4.9</span>
                    <span class="package-status status-approved">مُعتمد</span>
                </div>
            </div>

            <div class="package-card">
                <div class="package-header">
                    <span class="package-name">🌍 ترجمة</span>
                    <span class="package-version">v0.5.0</span>
                </div>
                <p class="package-desc">مكتبة ترجمة النصوص بين اللغات باستخدام APIs مجانية.</p>
                <div class="package-meta">
                    <span>👤 خالد</span>
                    <span>⬇ 98</span>
                    <span>⭐ 4.2</span>
                    <span class="package-status status-pending">قيد المراجعة</span>
                </div>
            </div>

            <div class="package-card">
                <div class="package-header">
                    <span class="package-name">🎮 العاب</span>
                    <span class="package-version">v1.0.0</span>
                </div>
                <p class="package-desc">أدوات بناء ألعاب بسيطة. رسم أشكال وتحريكها والتفاعل مع المستخدم.</p>
                <div class="package-meta">
                    <span>👤 عمر</span>
                    <span>⬇ 156</span>
                    <span>⭐ 4.6</span>
                    <span class="package-status status-approved">مُعتمد</span>
                </div>
            </div>

            <div class="package-card">
                <div class="package-header">
                    <span class="package-name">📧 بريد</span>
                    <span class="package-version">v1.1.0</span>
                </div>
                <p class="package-desc">إرسال بريد إلكتروني عبر SMTP. يدعم HTML والمرفقات.</p>
                <div class="package-meta">
                    <span>👤 فاطمة</span>
                    <span>⬇ 134</span>
                    <span>⭐ 4.4</span>
                    <span class="package-status status-approved">مُعتمد</span>
                </div>
            </div>
        </div>

        <!-- Upload Section -->
        <div class="upload-section" id="upload-area">
            <div style="font-size: 48px; margin-bottom: 16px;">📦</div>
            <h3 style="margin-bottom: 8px;">شارك مكتبتك مع المجتمع</h3>
            <p style="color: var(--text-muted); margin-bottom: 24px;">ارفع مكتبتك وبعد الموافقة عليها هتكون متاحة للجميع</p>

            <form id="upload-form" style="max-width: 500px; margin: 0 auto; text-align: right;">
                <div style="margin-bottom: 16px;">
                    <label style="display: block; margin-bottom: 6px; font-size: 14px; color: var(--text-light);">اسم المكتبة</label>
                    <input type="text" name="name" required placeholder="مثال: أدوات_رياضية"
                           style="width: 100%; padding: 10px 14px; border-radius: 8px; border: 1px solid var(--border); background: var(--surface-light); color: white; font-family: inherit;">
                </div>

                <div style="margin-bottom: 16px;">
                    <label style="display: block; margin-bottom: 6px; font-size: 14px; color: var(--text-light);">الوصف</label>
                    <textarea name="description" required placeholder="اشرح شنو المكتبة بتسوي..."
                              style="width: 100%; padding: 10px 14px; border-radius: 8px; border: 1px solid var(--border); background: var(--surface-light); color: white; font-family: inherit; height: 80px; resize: vertical;"></textarea>
                </div>

                <div style="margin-bottom: 16px;">
                    <label style="display: block; margin-bottom: 6px; font-size: 14px; color: var(--text-light);">الفئة</label>
                    <select name="category" style="width: 100%; padding: 10px 14px; border-radius: 8px; border: 1px solid var(--border); background: var(--surface-light); color: white; font-family: inherit;">
                        <option value="utils">أدوات</option>
                        <option value="math">رياضيات</option>
                        <option value="text">نصوص</option>
                        <option value="ui">واجهات</option>
                        <option value="data">بيانات</option>
                        <option value="network">شبكات</option>
                    </select>
                </div>

                <div style="margin-bottom: 16px;">
                    <label style="display: block; margin-bottom: 6px; font-size: 14px; color: var(--text-light);">الإصدار</label>
                    <input type="text" name="version" value="1.0.0"
                           style="width: 100%; padding: 10px 14px; border-radius: 8px; border: 1px solid var(--border); background: var(--surface-light); color: white; font-family: inherit;">
                </div>

                <div style="margin-bottom: 24px;">
                    <label style="display: block; margin-bottom: 6px; font-size: 14px; color: var(--text-light);">ملف المكتبة (.havnix أو .zip)</label>
                    <input type="file" name="package_file" accept=".havnix,.zip,.tar.gz" required
                           style="width: 100%; padding: 10px; border-radius: 8px; border: 1px solid var(--border); background: var(--surface-light); color: white;">
                </div>

                <button type="submit" class="btn btn-primary" style="width: 100%; justify-content: center;">
                    📤 رفع المكتبة للمراجعة
                </button>

                <p style="font-size: 12px; color: var(--text-muted); margin-top: 12px; text-align: center;">
                    سيتم مراجعة المكتبة من قبل فريق هافنيكس قبل نشرها
                </p>
            </form>
        </div>

        <!-- How to use packages -->
        <div class="install-steps" style="margin-top: 40px;">
            <h2 style="color: var(--accent); margin-bottom: 16px;">📖 كيف تستخدم المكتبات</h2>

            <div class="step">
                <div class="step-num">1</div>
                <div class="step-content">
                    <h4>حمّل المكتبة</h4>
                    <p>اضغط تحميل على صفحة المكتبة</p>
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
                    <div class="code-block" style="margin: 8px 0;">
                        <pre><span class="kw">استورد</span> <span class="str">"libs/رسوم_بيانية.havnix"</span><span class="op">;</span></pre>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
