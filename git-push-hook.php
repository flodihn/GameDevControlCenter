<html>
<head>
<title>Git Web Hook</title>
</head>
<body>

<?php
require_once("web_conf.php");

$passwd = $_POST['password'];

//if($passwd != $HOOK_PASSWD) die ("Invalid hook password");

$lockfile = "lockfile";
if(file_exists($lockfile)) die ("Update already in progress");

$myfile = fopen($lockfile, "w") or die("Unable to open lock file!");
fclose($myfile);


$output = shell_exec('./gdd_to_pdf.py');
echo "<pre>$output</pre>";
$output = shell_exec('./matrix_update.py');
echo "<pre>$output</pre>";
unlink($lockfile);
?>

</body>
</html>

