<?php $page_title = 'بنية اللغة - Havnix'; ?>

<div class="container">
    <div class="docs-layout">
        <?php include INCLUDES_PATH . '/docs-sidebar.php'; ?>

        <div class="docs-content">
            <h1>📐 بنية اللغة</h1>

            <h2>أنواع البيانات</h2>
            <table class="docs-table">
                <tr><th>النوع</th><th>المثال</th><th>الوصف</th></tr>
                <tr><td>نص</td><td><code>"مرحبا"</code></td><td>سلسلة نصية</td></tr>
                <tr><td>رقم صحيح</td><td><code>42</code></td><td>عدد صحيح</td></tr>
                <tr><td>رقم عشري</td><td><code>3.14</code></td><td>عدد عشري</td></tr>
                <tr><td>منطقي</td><td><code>صاح</code> / <code>غلط</code></td><td>قيمة صح أو خطأ</td></tr>
                <tr><td>فاضي</td><td><code>فاضي</code></td><td>قيمة فارغة (null)</td></tr>
                <tr><td>قائمة</td><td><code>[1, 2, 3]</code></td><td>مصفوفة</td></tr>
                <tr><td>قاموس</td><td><code>{"مفتاح": "قيمة"}</code></td><td>خريطة مفاتيح وقيم</td></tr>
            </table>

            <h2>العمليات الحسابية</h2>
            <table class="docs-table">
                <tr><th>العملية</th><th>الرمز</th><th>المثال</th></tr>
                <tr><td>جمع</td><td><code>+</code></td><td><code>5 + 3</code> → <code>8</code></td></tr>
                <tr><td>طرح</td><td><code>-</code></td><td><code>10 - 4</code> → <code>6</code></td></tr>
                <tr><td>ضرب</td><td><code>*</code></td><td><code>3 * 7</code> → <code>21</code></td></tr>
                <tr><td>قسمة</td><td><code>/</code></td><td><code>10 / 3</code> → <code>3.33</code></td></tr>
                <tr><td>باقي القسمة</td><td><code>%</code></td><td><code>10 % 3</code> → <code>1</code></td></tr>
            </table>

            <h2>عمليات المقارنة</h2>
            <table class="docs-table">
                <tr><th>العملية</th><th>الرمز</th><th>المثال</th></tr>
                <tr><td>يساوي</td><td><code>==</code></td><td><code>$أ == 5</code></td></tr>
                <tr><td>لا يساوي</td><td><code>!=</code></td><td><code>$أ != 5</code></td></tr>
                <tr><td>أكبر من</td><td><code>></code></td><td><code>$أ > 5</code></td></tr>
                <tr><td>أصغر من</td><td><code><</code></td><td><code>$أ < 5</code></td></tr>
                <tr><td>أكبر أو يساوي</td><td><code>>=</code></td><td><code>$أ >= 5</code></td></tr>
                <tr><td>أصغر أو يساوي</td><td><code><=</code></td><td><code>$أ <= 5</code></td></tr>
            </table>

            <h2>العمليات المنطقية</h2>
            <table class="docs-table">
                <tr><th>العملية</th><th>الكلمة</th><th>المثال</th></tr>
                <tr><td>و (AND)</td><td><code>و</code></td><td><code>$أ > 5 و $ب < 10</code></td></tr>
                <tr><td>أو (OR)</td><td><code>أو</code></td><td><code>$أ > 5 أو $ب < 10</code></td></tr>
                <tr><td>نفي (NOT)</td><td><code>مو</code></td><td><code>مو ($أ > 5)</code></td></tr>
            </table>

            <h2>القوائم (المصفوفات)</h2>
            <div class="code-block">
                <pre><span class="var">$أرقام</span> <span class="op">=</span> [<span class="num">1</span><span class="op">,</span> <span class="num">2</span><span class="op">,</span> <span class="num">3</span><span class="op">,</span> <span class="num">4</span><span class="op">,</span> <span class="num">5</span>]<span class="op">;</span>

<span class="cm">// الوصول لعنصر</span>
<span class="fn">قول ليهو</span>(<span class="var">$أرقام</span>[<span class="num">0</span>])<span class="op">;</span>  <span class="cm">// 1</span>

<span class="cm">// إضافة عنصر</span>
<span class="fn">اضف</span>(<span class="var">$أرقام</span><span class="op">,</span> <span class="num">6</span>)<span class="op">;</span>

<span class="cm">// طول القائمة</span>
<span class="fn">قول ليهو</span>(<span class="fn">طول</span>(<span class="var">$أرقام</span>))<span class="op">;</span>  <span class="cm">// 6</span></pre>
            </div>

            <h2>القواميس</h2>
            <div class="code-block">
                <pre><span class="var">$شخص</span> <span class="op">=</span> {
    <span class="str">"الاسم"</span><span class="op">:</span> <span class="str">"أحمد"</span><span class="op">,</span>
    <span class="str">"العمر"</span><span class="op">:</span> <span class="num">25</span><span class="op">,</span>
    <span class="str">"مدينة"</span><span class="op">:</span> <span class="str">"الخرطوم"</span>
}<span class="op">;</span>

<span class="fn">قول ليهو</span>(<span class="var">$شخص</span>[<span class="str">"الاسم"</span>])<span class="op">;</span>  <span class="cm">// أحمد</span></pre>
            </div>

            <h2>الكلمات المفتاحية</h2>
            <table class="docs-table">
                <tr><th>الكلمة</th><th>المعنى</th><th>المقابل الإنجليزي</th></tr>
                <tr><td><code>لو</code></td><td>شرط</td><td>if</td></tr>
                <tr><td><code>غير كدا لو</code></td><td>شرط بديل</td><td>else if</td></tr>
                <tr><td><code>غير كدا</code></td><td>بديل</td><td>else</td></tr>
                <tr><td><code>طالما</code></td><td>حلقة</td><td>while</td></tr>
                <tr><td><code>لكل</code></td><td>حلقة لكل عنصر</td><td>foreach</td></tr>
                <tr><td><code>تكرار</code></td><td>حلقة عددية</td><td>for</td></tr>
                <tr><td><code>دالة</code></td><td>تعريف دالة</td><td>function</td></tr>
                <tr><td><code>ارجع</code></td><td>إرجاع قيمة</td><td>return</td></tr>
                <tr><td><code>اقيف</code></td><td>إيقاف حلقة</td><td>break</td></tr>
                <tr><td><code>كمل</code></td><td>تخطي دورة</td><td>continue</td></tr>
                <tr><td><code>جرب</code></td><td>محاولة</td><td>try</td></tr>
                <tr><td><code>امسك</code></td><td>التقاط خطأ</td><td>catch</td></tr>
                <tr><td><code>واخيراً</code></td><td>تنفيذ نهائي</td><td>finally</td></tr>
                <tr><td><code>ثابت</code></td><td>تعريف ثابت</td><td>const</td></tr>
            </table>

            <div style="margin-top: 40px; padding: 20px; background: var(--surface-light); border-radius: 10px; border-right: 4px solid var(--accent);">
                <p><strong>التالي:</strong> تعرف على <a href="<?php echo SITE_URL; ?>/docs/functions">الدوال المدمجة</a></p>
            </div>
        </div>
    </div>
</div>
