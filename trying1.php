<?php

// Starting session
session_start();

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "buddyadvisor";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
$data = $_POST['variable'];

for( $i = 0; $i<sizeof($data); $i++ ) {
	$sql = "INSERT INTO data (longitude, latitude, type)
	VALUES (".$data[$i][0].",".$data[$i][1].", '".$data[$i][3]."')";


	if ($conn->query($sql) === TRUE) {
	    echo "New record created successfully".$data[$i][3];
	} else {
	    echo "Error: " . $sql . "<br>" . $conn->error;
	}
}



$conn->close();
?>