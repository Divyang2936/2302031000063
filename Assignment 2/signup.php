<?php
$host = "localhost";
$dbname = "writing_collab";
$username = "root";
$password = "Divyang@2936";

$conn = new mysqli($host, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars(trim($_POST["name"]));
    $email = htmlspecialchars(trim($_POST["email"]));
    $writing_style = htmlspecialchars(trim($_POST["writing_style"]));
    $bio = htmlspecialchars(trim($_POST["bio"]));
    $message = htmlspecialchars(trim($_POST["message"]));

    $stmt = $conn->prepare("INSERT INTO users (name, email, writing_style, bio, message) VALUES (?, ?, ?, ?, ?)");
    $stmt->bind_param("sssss", $name, $email, $writing_style, $bio, $message);

    if ($stmt->execute()) {
        // Redirect to home page
        header("Location: home2.html");
        exit();
    } else {
        echo "Error: " . $stmt->error;
    }

    $stmt->close();
}
$conn->close();
?>
