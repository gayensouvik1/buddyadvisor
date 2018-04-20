<!-- <?php 

$command = escapeshellcmd('/opt/lampp/htdocs/BTP/matching.py');
$output = shell_exec($command);
echo $output;

?> -->

<?php


$myid = $_POST['user_id'];
$myactivity = $_POST['type'];
$start_time = $_POST['starttime'];
$end_time = $_POST['endtime'];
// $myid = "OPqacBiKHFYoieOI2abLCdSLHYx1";
// $myactivity = "gym";


echo shell_exec("python /opt/lampp/htdocs/BTP/matching.py $myid $myactivity 2>&1");
?>