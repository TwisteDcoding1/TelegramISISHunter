<?php
//we make sure we dont have the PRE-AUTH Vulnerability
//if ($_POST["key"] != "mSqGObqxCmvEwooj3zaW:Q74vx9wDBhPtpoaN4lcf:kZqYEz5H5RwhxFHJml2v") {
//  exit;
//}
//Setup our input
$reportedUser = $_POST["user"];
$reportedID = $_POST["id"];
$reportedMsg = $_POST["msg"];

$servername = "mysql4.000webhost.com";
$username = "a3016441_root";
$password = "Vikings01";
$db = "a3016441_sus";

// Create connection
$conn = new mysqli($servername, $username, $password, $db);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";

$sql = "INSERT INTO tbl_suspects (username, suspectid, msg) VALUES ('$reportedUser','$reportedID','$reportedMsg')";
if ($conn->query($sql) === TRUE) {
    echo "Data Saved to DB";
} else {
    echo "Error: " . $conn->error;
}
?>
