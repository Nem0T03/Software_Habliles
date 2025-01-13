<?php 
$host = 'sql210.byethost9.com';
$username = 'b9_38010536';
$password = 'Binh1234@';
$database = 'b9_38010536_web';

$con = new mysqli($host, $username, $password, $database);

if ($con->connect_error) {
    die("Connection failed: " . $con->connect_error);
} else  {
    echo "Connection full";
}
?>
