<?php
$flag = $_GET['flag'] ?? null;
if(!empty($flag)){
    $xx = mb_list_encodings(); 
    $xx = array("1337" => $xx[3]);
    $flag = mb_convert_encoding($flag, 'UTF-8', $xx["1337"]);
    $flag = base64_encode($flag);
    echo "<h1>The baby encoder!</h1>
    Your encoded flag is <strong>$flag</strong>";
} else {
    die("Missing parameters!");
}
