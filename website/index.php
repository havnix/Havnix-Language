<?php
/**
 * Havnix Website - Main Router
 * Slug-based URL routing
 * Works on XAMPP, Apache, Nginx, and PHP built-in server
 */

require_once __DIR__ . '/config.php';

// Get the slug from URL - support both .htaccess rewrite and direct access
if (isset($_GET['slug'])) {
    $slug = trim($_GET['slug'], '/');
} else {
    // Fallback: parse from REQUEST_URI (for servers without .htaccess)
    $uri = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
    $scriptDir = str_replace('\\', '/', dirname($_SERVER['SCRIPT_NAME']));
    if ($scriptDir !== '/' && $scriptDir !== '.') {
        $slug = substr($uri, strlen($scriptDir));
    } else {
        $slug = $uri;
    }
    $slug = trim($slug, '/');
    // Remove index.php if present
    if (strpos($slug, 'index.php') === 0) {
        $slug = '';
    }
}

$slug = $slug ?: 'home';

// Define routes
$routes = [
    'home'           => 'pages/home.php',
    'docs'           => 'pages/docs.php',
    'docs/start'     => 'pages/docs-start.php',
    'docs/syntax'    => 'pages/docs-syntax.php',
    'docs/functions' => 'pages/docs-functions.php',
    'docs/advanced'  => 'pages/docs-advanced.php',
    'docs/packages'  => 'pages/docs-packages.php',
    'download'       => 'pages/download.php',
    'marketplace'    => 'pages/marketplace.php',
    'about'          => 'pages/about.php',
    'help'           => 'pages/help.php',
];

// Check if route exists
if (isset($routes[$slug])) {
    $page_file = ROOT_PATH . '/' . $routes[$slug];
} else {
    http_response_code(404);
    $page_file = ROOT_PATH . '/pages/404.php';
}

// Page meta defaults
$page_title = SITE_NAME;
$page_description = SITE_DESC;

// Buffer the page content (so it can set $page_title before header renders)
ob_start();
if (file_exists($page_file)) {
    include $page_file;
} else {
    echo '<div class="container"><h1>الصفحة غير موجودة</h1></div>';
}
$page_content = ob_get_clean();

// Include header (now $page_title is set by the page)
include INCLUDES_PATH . '/header.php';

// Output page content
echo $page_content;

// Include footer
include INCLUDES_PATH . '/footer.php';
