<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo htmlspecialchars($page_title); ?></title>
    <meta name="description" content="<?php echo htmlspecialchars($page_description); ?>">
    <link rel="stylesheet" href="<?php echo SITE_URL; ?>/assets/css/style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lipis/flag-icons@7.0.0/css/flag-icons.min.css">
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='80'>H</text></svg>">
</head>
<body>

<nav class="navbar">
    <div class="nav-inner">
        <a href="<?php echo SITE_URL; ?>/" class="nav-logo">
            <img src="<?php echo SITE_URL; ?>/assets/images/logo.png" alt="Havnix Logo" class="logo-img" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
            <span class="logo-fallback" style="display:none; width:36px; height:36px; background:linear-gradient(180deg,#000,#1B569A); border-radius:8px; align-items:center; justify-content:center; color:white; font-weight:900; font-size:18px;">H</span>
            Havnix
        </a>

        <button class="nav-toggle" onclick="document.querySelector('.nav-links').classList.toggle('open')"><i class="fas fa-bars"></i></button>

        <ul class="nav-links">
            <li><a href="<?php echo SITE_URL; ?>/" <?php echo $slug === 'home' ? 'class="active"' : ''; ?>><i class="fas fa-home"></i> الرئيسية</a></li>
            <li><a href="<?php echo SITE_URL; ?>/docs" <?php echo strpos($slug, 'docs') === 0 ? 'class="active"' : ''; ?>><i class="fas fa-book"></i> التوثيق</a></li>
            <li><a href="<?php echo SITE_URL; ?>/download" <?php echo $slug === 'download' ? 'class="active"' : ''; ?>><i class="fas fa-download"></i> تحميل</a></li>
            <li><a href="<?php echo SITE_URL; ?>/marketplace" <?php echo $slug === 'marketplace' ? 'class="active"' : ''; ?>><i class="fas fa-store"></i> المكتبات</a></li>
            <li><a href="<?php echo SITE_URL; ?>/help" <?php echo $slug === 'help' ? 'class="active"' : ''; ?>><i class="fas fa-circle-question"></i> مساعدة</a></li>
            <li><a href="<?php echo SITE_URL; ?>/about" <?php echo $slug === 'about' ? 'class="active"' : ''; ?>><i class="fas fa-info-circle"></i> حول</a></li>
            <li><a href="https://github.com/Snixrs/Havnix-Language" target="_blank" class="nav-cta"><i class="fab fa-github"></i> GitHub</a></li>
        </ul>
    </div>
</nav>
