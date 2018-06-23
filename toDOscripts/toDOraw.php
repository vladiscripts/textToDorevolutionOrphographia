<?php
if (isset($_POST["text"])) {
	require 'toDO.php';	
	$t = $_POST["text"];
	$t = $page2DO->convert($t);
	echo $t;
}