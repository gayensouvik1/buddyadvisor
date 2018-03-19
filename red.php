
<?php
// Starting session
session_start();
 
// Storing session data
$_SESSION["firstname"] = $_POST['name'];
$_SESSION["lastname"] = "Parker";
header("Location:trying.php");
?>

