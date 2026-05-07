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
                    <span class="pkg-name"><i class="fas fa-calendar-alt" style="color: var(--accent);"></i> التقويم_الهجري</span>
                    <span class="pkg-version">v1.0.0</span>
                </div>
                <p class="pkg-desc">تحويل التواريخ الميلادية إلى هجرية، أسماء الأشهر والأيام بالعربي.</p>
                <div class="pkg-meta">
                    <span><i class="fas fa-user"></i> Havnix Team</span>
                    <span><i class="fas fa-terminal"></i> <code style="font-size: 11px;">havnix install التقويم_الهجري</code></span>
                    <span class="pkg-status approved"><i class="fas fa-check-circle"></i> رسمية</span>
                </div>
            </div>

            <div class="package-card" data-category="math">
                <div class="pkg-header">
                    <span class="pkg-name"><i class="fas fa-calculator" style="color: var(--accent);"></i> الرياضيات_المتقدمة</span>
                    <span class="pkg-version">v1.0.0</span>
                </div>
                <p class="pkg-desc">قوة، مضروب، متوسط، وسيط، أعداد أولية، فيبوناتشي، ق.م.أ، م.م.أ.</p>
                <div class="pkg-meta">
                    <span><i class="fas fa-user"></i> Havnix Team</span>
                    <span><i class="fas fa-terminal"></i> <code style="font-size: 11px;">havnix install الرياضيات_المتقدمة</code></span>
                    <span class="pkg-status approved"><i class="fas fa-check-circle"></i> رسمية</span>
                </div>
            </div>

            <div class="package-card" data-category="text">
                <div class="pkg-header">
                    <span class="pkg-name"><i class="fas fa-font" style="color: var(--accent);"></i> معالج_النصوص</span>
                    <span class="pkg-version">v1.0.0</span>
                </div>
                <p class="pkg-desc">عكس نص، عد كلمات وحروف، بحث، اقتطاع، تنظيف، دمج نصوص.</p>
                <div class="pkg-meta">
                    <span><i class="fas fa-user"></i> Havnix Team</span>
                    <span><i class="fas fa-terminal"></i> <code style="font-size: 11px;">havnix install معالج_النصوص</code></span>
                    <span class="pkg-status approved"><i class="fas fa-check-circle"></i> رسمية</span>
                </div>
            </div>

            <div class="package-card" data-category="utils">
                <div class="pkg-header">
                    <span class="pkg-name"><i class="fas fa-palette" style="color: var(--accent);"></i> الألوان</span>
                    <span class="pkg-version">v1.0.0</span>
                </div>
                <p class="pkg-desc">طباعة ملونة في الطرفية، رسائل نجاح وخطأ وتحذير مزخرفة.</p>
                <div class="pkg-meta">
                    <span><i class="fas fa-user"></i> Havnix Team</span>
                    <span><i class="fas fa-terminal"></i> <code style="font-size: 11px;">havnix install الألوان</code></span>
                    <span class="pkg-status approved"><i class="fas fa-check-circle"></i> رسمية</span>
                </div>
            </div>

            <div class="package-card" data-category="utils">
                <div class="pkg-header">
                    <span class="pkg-name"><i class="fas fa-check-double" style="color: var(--accent);"></i> التحقق</span>
                    <span class="pkg-version">v1.0.0</span>
                </div>
                <p class="pkg-desc">تحقق من بريد إلكتروني، هاتف، كلمة مرور قوية، أرقام، نطاقات.</p>
                <div class="pkg-meta">
                    <span><i class="fas fa-user"></i> Havnix Team</span>
                    <span><i class="fas fa-terminal"></i> <code style="font-size: 11px;">havnix install التحقق</code></span>
                    <span class="pkg-status approved"><i class="fas fa-check-circle"></i> رسمية</span>
                </div>
            </div>

            <div class="package-card" data-category="data">
                <div class="pkg-header">
                    <span class="pkg-name"><i class="fas fa-folder-open" style="color: var(--accent);"></i> أدوات_الملفات</span>
                    <span class="pkg-version">v1.0.0</span>
                </div>
                <p class="pkg-desc">قراءة وكتابة ملفات، JSON، CSV، سجلات، نسخ ملفات.</p>
                <div class="pkg-meta">
                    <span><i class="fas fa-user"></i> Havnix Team</span>
                    <span><i class="fas fa-terminal"></i> <code style="font-size: 11px;">havnix install أدوات_الملفات</code></span>
                    <span class="pkg-status approved"><i class="fas fa-check-circle"></i> رسمية</span>
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
