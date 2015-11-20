<?php
//we make sure we dont have the PRE-AUTH Vulnerability
//if ($_POST["key"] != "mSqGObqxCmvEwooj3zaW:Q74vx9wDBhPtpoaN4lcf:kZqYEz5H5RwhxFHJml2v") {
//  exit;
//}
//Setup our input

header('Content-Type: application/json');
$servername = "DBSERVER";
$username = "DBUSERNAME";
$password = "PASSWD";
$db = "DBNAME";

// Create connection
$conn = new mysqli($servername, $username, $password, $db);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT * FROM tbl_suspects ORDER BY rand() LIMIT 1";
$result = $conn->query($sql);
while($r = mysqli_fetch_assoc($result)) {
    $rows[] = $r;
}
echo json_encode($rows);
?>
