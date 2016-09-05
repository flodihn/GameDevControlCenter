<html>
<head>
<title>Git Web Hook</title>
</head>
<body>

<?php
$lockfile = "lockfile";
if(file_exists($lockfile)) die ("Update already in progress");

$myfile = fopen($lockfile, "w") or die("Unable to open lock file!");
fclose($myfile);


$output = shell_exec('./game_doc_matrix_update.py');
echo "<pre>$output</pre>";
unlink($lockfile);
?>

</body>
</html>

