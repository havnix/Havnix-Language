<?php
/**
 * Havnix Website Configuration
 */

// Database Configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'havnix_db');
define('DB_USER', 'root');
define('DB_PASS', '');

// Site Configuration
define('SITE_NAME', 'Havnix');
define('SITE_DESC', 'لغة برمجة بالعربية السودانية');
define('SITE_URL', 'http://localhost:8080');
define('SITE_VERSION', '1.0.0');

// Paths
define('ROOT_PATH', __DIR__);
define('PAGES_PATH', ROOT_PATH . '/pages');
define('INCLUDES_PATH', ROOT_PATH . '/includes');
define('UPLOADS_PATH', ROOT_PATH . '/uploads');

// Marketplace settings
define('MAX_UPLOAD_SIZE', 10 * 1024 * 1024); // 10MB
define('ALLOWED_EXTENSIONS', 'zip,tar.gz,havnix');

// Database connection
function getDB() {
    static $pdo = null;
    if ($pdo === null) {
        try {
            $pdo = new PDO(
                "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME . ";charset=utf8mb4",
                DB_USER,
                DB_PASS,
                [
                    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
                    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
                    PDO::MYSQL_ATTR_INIT_COMMAND => "SET NAMES utf8mb4"
                ]
            );
        } catch (PDOException $e) {
            // Database not available - work without it
            $pdo = false;
        }
    }
    return $pdo;
}
