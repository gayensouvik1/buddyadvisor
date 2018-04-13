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
	$d=$data[$i][4].'/'.$data[$i][3].'/'.$data[$i][2];
	$t=($data[$i][6]<10?'0':'').$data[$i][6].':'.($data[$i][7]<10?'0':'').$data[$i][7].':00';
	$sql = "INSERT INTO data (user_id, longitude, latitude, placetype, date, time)
	VALUES (1,".$data[$i][1].",".$data[$i][0].",'".$data[$i][8]."','".date($d)."','".$t."');"; 


	if ($conn->query($sql) === TRUE) {
	    echo "New record created successfully".date($d);
	} else {
	    echo "Error: " . $sql . "<br>" . $conn->error;
	}
}



$conn->close();
?>