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
                <div class="os-icon"><i class="fab fa-windows" style="color: #0078D4;"></i></div>
                <h3>Windows</h3>
                <p>Windows 10/11 - 64-bit<br>يتضمن Python المدمج + IDE</p>
                <a href="https://github.com/Snixrs/Havnix-Language/releases/latest" target="_blank" class="btn btn-primary" style="margin-bottom: 8px;">
                    <i class="fas fa-download"></i> تحميل HavnixSetup.exe
                </a>
                <p style="font-size: 12px; color: var(--text-muted); margin-top: 12px;">~25 MB | يتطلب صلاحيات مدير</p>
            </div>

            <!-- Linux -->
            <div class="download-card">
                <div class="os-icon"><i class="fab fa-linux" style="color: #FCC624;"></i></div>
                <h3>Linux</h3>
                <p>Ubuntu, Debian, Fedora, Arch<br>DEB + RPM + تثبيت يدوي</p>
                <a href="https://github.com/Snixrs/Havnix-Language/releases/latest" target="_blank" class="btn btn-primary" style="margin-bottom: 8px;">
                    <i class="fas fa-download"></i> تحميل havnix-linux.tar.gz
                </a>
                <p style="font-size: 12px; color: var(--text-muted); margin-top: 12px;">~15 MB | يتطلب Python 3.8+</p>
            </div>

            <!-- macOS -->
            <div class="download-card">
                <div class="os-icon"><i class="fab fa-apple" style="color: #999;"></i></div>
                <h3>macOS</h3>
                <p>macOS 11+ (Big Sur وأحدث)<br>Intel + Apple Silicon</p>
                <a href="https://github.com/Snixrs/Havnix-Language/releases/latest" target="_blank" class="btn btn-primary" style="margin-bottom: 8px;">
                    <i class="fas fa-download"></i> تحميل Havnix.dmg
                </a>
                <p style="font-size: 12px; color: var(--text-muted); margin-top: 12px;">~20 MB | يتطلب Python 3.8+</p>
            </div>
        </div>

        <!-- Manual Install -->
        <div class="install-steps">
            <h2 style="color: var(--accent);"><i class="fas fa-box-open"></i> تثبيت يدوي (كل الأنظمة)</h2>
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
            <h2 style="color: var(--accent);"><i class="fas fa-hammer"></i> بناء ملف setup.exe بنفسك</h2>
            <p style="color: var(--text-muted); margin-bottom: 24px;">اصنع مثبّت هافنيكس الخاص بك</p>

            <h4 style="margin-bottom: 8px;">الطريقة 1: PyInstaller (كل الأنظمة)</h4>
            <div class="code-block" style="direction: ltr; text-align: left; margin-bottom: 16px;">
                <pre># Windows
installer\build_installer.bat

# Linux / macOS
chmod +x installer/build_installer.sh
./installer/build_installer.sh

# النتيجة: dist/havnix-setup.exe (أو dist/havnix-setup)</pre>
            </div>

            <h4 style="margin-bottom: 8px;">الطريقة 2: Inno Setup (Windows فقط - مثبت احترافي)</h4>
            <div class="code-block" style="direction: ltr; text-align: left; margin-bottom: 16px;">
                <pre># 1. حمّل Inno Setup: https://jrsoftware.org/isinfo.php
# 2. افتح: installer/havnix_setup.iss
# 3. اضغط Compile
# النتيجة: havnix-setup.exe (مثبت Windows احترافي مع:
#   - إضافة تلقائية لـ PATH
#   - اختصارات سطح المكتب + Start Menu
#   - ربط ملفات .havnix
#   - uninstall.exe
#   - تثبيت المتطلبات تلقائياً)</pre>
            </div>

            <h4 style="margin-bottom: 8px;">الطريقة 3: Python مباشرة</h4>
            <div class="code-block" style="direction: ltr; text-align: left;">
                <pre>python3 installer/havnix_installer.py</pre>
            </div>
        </div>

        <!-- What Setup Includes -->
        <div class="install-steps" style="margin-top: 24px;">
            <h2 style="color: var(--accent);"><i class="fas fa-box"></i> ماذا يتضمن المثبّت؟</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin-top: 16px;">
                <div style="padding: 16px; background: var(--bg-dark); border-radius: 12px; border: 1px solid var(--border);">
                    <i class="fas fa-code" style="color: var(--accent); font-size: 24px; margin-bottom: 8px;"></i>
                    <h4>مفسر هافنيكس</h4>
                    <p style="font-size: 13px; color: var(--text-muted);">havnix.py + أوامر CLI</p>
                </div>
                <div style="padding: 16px; background: var(--bg-dark); border-radius: 12px; border: 1px solid var(--border);">
                    <i class="fas fa-laptop-code" style="color: var(--accent); font-size: 24px; margin-bottom: 8px;"></i>
                    <h4>IDE متكامل</h4>
                    <p style="font-size: 13px; color: var(--text-muted);">محرر + طرفية + مستكشف ملفات</p>
                </div>
                <div style="padding: 16px; background: var(--bg-dark); border-radius: 12px; border: 1px solid var(--border);">
                    <i class="fas fa-cubes" style="color: var(--accent); font-size: 24px; margin-bottom: 8px;"></i>
                    <h4>6 مكتبات جاهزة</h4>
                    <p style="font-size: 13px; color: var(--text-muted);">رياضيات، تقويم، ألوان، ...</p>
                </div>
                <div style="padding: 16px; background: var(--bg-dark); border-radius: 12px; border: 1px solid var(--border);">
                    <i class="fas fa-route" style="color: var(--accent); font-size: 24px; margin-bottom: 8px;"></i>
                    <h4>PATH تلقائي</h4>
                    <p style="font-size: 13px; color: var(--text-muted);">اكتب <code>havnix</code> من أي مكان</p>
                </div>
                <div style="padding: 16px; background: var(--bg-dark); border-radius: 12px; border: 1px solid var(--border);">
                    <i class="fas fa-file-alt" style="color: var(--accent); font-size: 24px; margin-bottom: 8px;"></i>
                    <h4>ربط .havnix</h4>
                    <p style="font-size: 13px; color: var(--text-muted);">دبل كليك يشغل الملف</p>
                </div>
                <div style="padding: 16px; background: var(--bg-dark); border-radius: 12px; border: 1px solid var(--border);">
                    <i class="fas fa-trash-alt" style="color: var(--accent); font-size: 24px; margin-bottom: 8px;"></i>
                    <h4>إزالة نظيفة</h4>
                    <p style="font-size: 13px; color: var(--text-muted);">uninstall.exe لإزالة كل شي</p>
                </div>
            </div>
        </div>
    </div>
</section>
