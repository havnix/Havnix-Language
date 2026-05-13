<?php
/**
 * Havnix Marketplace - Packages API
 * GET /api/packages.php?category=&search=
 */

header('Content-Type: application/json; charset=utf-8');

require_once __DIR__ . '/../config.php';

$db = getDB();

if (!$db) {
    // Return sample data when database is not available
    echo json_encode([
        'packages' => [
            [
                'id' => 1,
                'name' => 'رسوم_بيانية',
                'slug' => 'charts',
                'description' => 'مكتبة لرسم الأشكال البيانية والمخططات',
                'version' => '1.0.0',
                'author' => 'أحمد',
                'downloads' => 245,
                'rating' => 4.5,
                'status' => 'approved',
                'category' => 'utils'
            ],
            [
                'id' => 2,
                'name' => 'تشفير',
                'slug' => 'crypto',
                'description' => 'أدوات تشفير وفك تشفير النصوص',
                'version' => '2.1.0',
                'author' => 'محمد',
                'downloads' => 189,
                'rating' => 4.8,
                'status' => 'approved',
                'category' => 'utils'
            ],
            [
                'id' => 3,
                'name' => 'تاريخ_هجري',
                'slug' => 'hijri-date',
                'description' => 'تحويل بين التاريخ الهجري والميلادي',
                'version' => '1.2.0',
                'author' => 'علي',
                'downloads' => 320,
                'rating' => 4.9,
                'status' => 'approved',
                'category' => 'utils'
            ]
        ],
        'total' => 3,
        'source' => 'sample'
    ]);
    exit;
}

// Build query
$where = ["status = 'approved'"];
$params = [];

$category = $_GET['category'] ?? '';
if (!empty($category)) {
    $where[] = "category = :category";
    $params[':category'] = $category;
}

$search = $_GET['search'] ?? '';
if (!empty($search)) {
    $where[] = "(name LIKE :search OR description LIKE :search2)";
    $params[':search'] = "%$search%";
    $params[':search2'] = "%$search%";
}

$whereClause = implode(' AND ', $where);
$sql = "SELECT p.*, u.display_name as author FROM packages p
        LEFT JOIN users u ON p.author_id = u.id
        WHERE $whereClause ORDER BY downloads DESC";

try {
    $stmt = $db->prepare($sql);
    $stmt->execute($params);
    $packages = $stmt->fetchAll();

    echo json_encode([
        'packages' => $packages,
        'total' => count($packages),
        'source' => 'database'
    ]);
} catch (PDOException $e) {
    http_response_code(500);
    echo json_encode(['error' => 'خطأ في جلب البيانات']);
}
