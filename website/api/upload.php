<?php
/**
 * Havnix Marketplace - Package Upload API
 * POST /api/upload.php
 */

header('Content-Type: application/json; charset=utf-8');

require_once __DIR__ . '/../config.php';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['error' => 'Method not allowed']);
    exit;
}

// Validate inputs
$name = trim($_POST['name'] ?? '');
$description = trim($_POST['description'] ?? '');
$category = trim($_POST['category'] ?? 'utils');
$version = trim($_POST['version'] ?? '1.0.0');

if (empty($name) || empty($description)) {
    http_response_code(400);
    echo json_encode(['error' => 'الاسم والوصف مطلوبين']);
    exit;
}

// Validate file
if (!isset($_FILES['package_file']) || $_FILES['package_file']['error'] !== UPLOAD_ERR_OK) {
    http_response_code(400);
    echo json_encode(['error' => 'يجب رفع ملف المكتبة']);
    exit;
}

$file = $_FILES['package_file'];
$ext = strtolower(pathinfo($file['name'], PATHINFO_EXTENSION));
$allowed = ['havnix', 'zip', 'gz'];

if (!in_array($ext, $allowed)) {
    http_response_code(400);
    echo json_encode(['error' => 'نوع الملف غير مسموح. استخدم .havnix أو .zip']);
    exit;
}

if ($file['size'] > MAX_UPLOAD_SIZE) {
    http_response_code(400);
    echo json_encode(['error' => 'حجم الملف كبير جداً (الحد الأقصى 10MB)']);
    exit;
}

// Generate slug
$slug = preg_replace('/[^\p{L}\p{N}_-]/u', '-', $name);
$slug = trim($slug, '-');

// Save file
$filename = $slug . '_' . $version . '.' . $ext;
$filepath = UPLOADS_PATH . '/packages/' . $filename;
move_uploaded_file($file['tmp_name'], $filepath);

// Save to database (if available)
$db = getDB();
if ($db) {
    try {
        $stmt = $db->prepare("INSERT INTO packages (name, slug, description, version, category, file_path, file_size, status)
                              VALUES (:name, :slug, :desc, :version, :category, :filepath, :size, 'pending')");
        $stmt->execute([
            ':name' => $name,
            ':slug' => $slug,
            ':desc' => $description,
            ':version' => $version,
            ':category' => $category,
            ':filepath' => $filename,
            ':size' => $file['size'],
        ]);

        echo json_encode([
            'success' => true,
            'message' => 'تم رفع المكتبة بنجاح. سيتم مراجعتها قريباً.',
            'package_id' => $db->lastInsertId()
        ]);
    } catch (PDOException $e) {
        http_response_code(500);
        echo json_encode(['error' => 'خطأ في حفظ البيانات']);
    }
} else {
    // No database - just confirm file saved
    echo json_encode([
        'success' => true,
        'message' => 'تم رفع الملف. سيتم مراجعته عند تفعيل قاعدة البيانات.',
        'file' => $filename
    ]);
}
