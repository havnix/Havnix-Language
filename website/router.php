<?php
/**
 * Router for PHP built-in development server
 * Usage: php -S localhost:8080 router.php
 */

$uri = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

// Serve static files directly
$staticFile = __DIR__ . $uri;
if ($uri !== '/' && file_exists($staticFile) && is_file($staticFile)) {
    // Set content type for known extensions
    $ext = pathinfo($staticFile, PATHINFO_EXTENSION);
    $mimeTypes = [
        'css'  => 'text/css',
        'js'   => 'application/javascript',
        'png'  => 'image/png',
        'jpg'  => 'image/jpeg',
        'jpeg' => 'image/jpeg',
        'gif'  => 'image/gif',
        'svg'  => 'image/svg+xml',
        'ico'  => 'image/x-icon',
        'woff' => 'font/woff',
        'woff2' => 'font/woff2',
        'ttf'  => 'font/ttf',
    ];
    if (isset($mimeTypes[$ext])) {
        header('Content-Type: ' . $mimeTypes[$ext]);
    }
    return false; // Let PHP serve the file
}

// Route everything else through index.php
$slug = trim($uri, '/');
$_GET['slug'] = $slug;
require __DIR__ . '/index.php';
