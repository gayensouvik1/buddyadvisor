<!-- <?php 

$command = escapeshellcmd('/opt/lampp/htdocs/BTP/matching.py');
$output = shell_exec($command);
echo $output;

?> -->

<?php
// outputs the username that owns the running php/httpd process
// (on a system with the "whoami" executable in the path)
$myid = 1;
$myactivity = "gym";

echo shell_exec("python /opt/lampp/htdocs/BTP/matching.py $myid $myactivity ");
?>