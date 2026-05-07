<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo htmlspecialchars($page_title); ?></title>
    <meta name="description" content="<?php echo htmlspecialchars($page_description); ?>">
    <link rel="stylesheet" href="<?php echo SITE_URL; ?>/assets/css/style.css">
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='80'>H</text></svg>">
</head>
<body>

<nav class="navbar">
    <div class="nav-inner">
        <a href="<?php echo SITE_URL; ?>/" class="nav-logo">
            <svg viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect width="40" height="40" rx="8" fill="url(#logo-grad)"/>
                <text x="50%" y="55%" text-anchor="middle" dominant-baseline="middle" fill="white" font-size="22" font-weight="900" font-family="Arial">H</text>
                <defs>
                    <linearGradient id="logo-grad" x1="0" y1="0" x2="0" y2="1">
                        <stop offset="0%" stop-color="#000000"/>
                        <stop offset="100%" stop-color="#1B569A"/>
                    </linearGradient>
                </defs>
            </svg>
            Havnix
        </a>

        <button class="nav-toggle" onclick="document.querySelector('.nav-links').classList.toggle('open')">☰</button>

        <ul class="nav-links">
            <li><a href="<?php echo SITE_URL; ?>/" <?php echo $slug === 'home' ? 'class="active"' : ''; ?>>الرئيسية</a></li>
            <li><a href="<?php echo SITE_URL; ?>/docs" <?php echo strpos($slug, 'docs') === 0 ? 'class="active"' : ''; ?>>التوثيق</a></li>
            <li><a href="<?php echo SITE_URL; ?>/download" <?php echo $slug === 'download' ? 'class="active"' : ''; ?>>تحميل</a></li>
            <li><a href="<?php echo SITE_URL; ?>/marketplace" <?php echo $slug === 'marketplace' ? 'class="active"' : ''; ?>>المكتبات</a></li>
            <li><a href="<?php echo SITE_URL; ?>/about" <?php echo $slug === 'about' ? 'class="active"' : ''; ?>>حول</a></li>
            <li><a href="https://github.com/Snixrs/Havnix-Language" target="_blank" class="nav-cta">GitHub ★</a></li>
        </ul>
    </div>
</nav>
