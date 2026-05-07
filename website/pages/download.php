<?php $page_title = 'تحميل هافنيكس - Havnix Download'; ?>

<section class="download-hero">
    <div class="container">
        <h1 style="font-size: 42px; margin-bottom: 16px;">حمّل هافنيكس</h1>
        <p style="color: var(--text-light); font-size: 18px;">اختر نظام التشغيل وابدأ البرمجة بالسودانية</p>
        <p style="color: var(--text-muted); font-size: 14px; margin-top: 8px;">الإصدار الحالي: <?php echo SITE_VERSION; ?></p>
    </div>
</section>

<section style="padding: 0 0 60px; background: var(--bg-dark);">
    <div class="container">
        <div class="download-cards">
            <!-- Windows -->
            <div class="download-card">
                <div class="os-icon">🪟</div>
                <h3>Windows</h3>
                <p>Windows 10/11 - 64-bit<br>يتضمن Python المدمج + IDE</p>
                <a href="https://github.com/Snixrs/Havnix-Language/releases/latest" target="_blank" class="btn btn-primary" style="margin-bottom: 8px;">
                    ⬇ تحميل HavnixSetup.exe
                </a>
                <p style="font-size: 12px; color: var(--text-muted); margin-top: 12px;">~25 MB | يتطلب صلاحيات مدير</p>
            </div>

            <!-- Linux -->
            <div class="download-card">
                <div class="os-icon">🐧</div>
                <h3>Linux</h3>
                <p>Ubuntu, Debian, Fedora, Arch<br>DEB + RPM + تثبيت يدوي</p>
                <a href="https://github.com/Snixrs/Havnix-Language/releases/latest" target="_blank" class="btn btn-primary" style="margin-bottom: 8px;">
                    ⬇ تحميل havnix-linux.tar.gz
                </a>
                <p style="font-size: 12px; color: var(--text-muted); margin-top: 12px;">~15 MB | يتطلب Python 3.8+</p>
            </div>

            <!-- macOS -->
            <div class="download-card">
                <div class="os-icon">🍎</div>
                <h3>macOS</h3>
                <p>macOS 11+ (Big Sur وأحدث)<br>Intel + Apple Silicon</p>
                <a href="https://github.com/Snixrs/Havnix-Language/releases/latest" target="_blank" class="btn btn-primary" style="margin-bottom: 8px;">
                    ⬇ تحميل Havnix.dmg
                </a>
                <p style="font-size: 12px; color: var(--text-muted); margin-top: 12px;">~20 MB | يتطلب Python 3.8+</p>
            </div>
        </div>

        <!-- Manual Install -->
        <div class="install-steps">
            <h2 style="color: var(--accent);">📦 تثبيت يدوي (كل الأنظمة)</h2>
            <p style="color: var(--text-muted); margin-bottom: 24px;">إذا تفضل التثبيت اليدوي أو عندك Python مثبت مسبقاً</p>

            <div class="step">
                <div class="step-num">1</div>
                <div class="step-content">
                    <h4>تأكد من وجود Python</h4>
                    <div class="code-block" style="margin: 8px 0; direction: ltr; text-align: left;">
                        <pre>python3 --version   # يجب أن يكون 3.8 أو أعلى</pre>
                    </div>
                </div>
            </div>

            <div class="step">
                <div class="step-num">2</div>
                <div class="step-content">
                    <h4>حمّل المشروع</h4>
                    <div class="code-block" style="margin: 8px 0; direction: ltr; text-align: left;">
                        <pre>git clone https://github.com/Snixrs/Havnix-Language.git
cd Havnix-Language</pre>
                    </div>
                </div>
            </div>

            <div class="step">
                <div class="step-num">3</div>
                <div class="step-content">
                    <h4>ثبّت المتطلبات (اختياري)</h4>
                    <div class="code-block" style="margin: 8px 0; direction: ltr; text-align: left;">
                        <pre>pip install -r requirements.txt</pre>
                    </div>
                </div>
            </div>

            <div class="step">
                <div class="step-num">4</div>
                <div class="step-content">
                    <h4>شغّل IDE</h4>
                    <div class="code-block" style="margin: 8px 0; direction: ltr; text-align: left;">
                        <pre>python3 ide.py     # يفتح المتصفح تلقائياً على localhost:249</pre>
                    </div>
                </div>
            </div>

            <div class="step">
                <div class="step-num">5</div>
                <div class="step-content">
                    <h4>أو شغّل ملف مباشرة</h4>
                    <div class="code-block" style="margin: 8px 0; direction: ltr; text-align: left;">
                        <pre>python3 havnix.py examples/hello.havnix</pre>
                    </div>
                </div>
            </div>
        </div>

        <!-- Build EXE -->
        <div class="install-steps" style="margin-top: 24px;">
            <h2 style="color: var(--accent);">🔨 بناء ملف EXE بنفسك</h2>
            <p style="color: var(--text-muted); margin-bottom: 24px;">اصنع نسختك المحمولة من هافنيكس</p>

            <div class="code-block" style="direction: ltr; text-align: left;">
                <pre>pip install pyinstaller
python3 build_exe.py
# الملف التنفيذي: dist/HavnixIDE.exe</pre>
            </div>
        </div>
    </div>
</section>
