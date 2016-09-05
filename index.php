<html>
<head>
<title>GameDev Control Center</title>
</head>
<body>
<?php
include("web_conf.php");
?>
<div align="center">
	<div style="width: 800">
		<h1>Welcome to the Game Dev Control Center</h1>
		<?php
		echo "<h2>Game Name: " . $GAME_NAME . "</h2>";
		echo "<h2>Project Stage: " . $PROJECT_STAGE. "</h2>";
		?>
		On this page you can see the game project status. The documentation matrix below shows a list of all features found in the game design document and source code, and prints if they are implmente, not implmented, tested or not tested.
		<p>
		Here is a <a href="GDD.pdf">link</a> to the Game Design Document, which contains information about the features in detail.
		<p>
		<iframe src="matrix.pdf" width="800" height="600"></iframe>
		<p>
		All the information on this page will be automatically re-generated when the Game Design Document and source code for the game is updated.
	</div>
</div>
</body>
</html>
