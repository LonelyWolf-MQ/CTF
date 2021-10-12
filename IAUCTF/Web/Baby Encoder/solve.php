<?php
$flag = "5KSg5ZWB5rGm5p2h44m75piw5oi044i545mi5oi045y55oiy5omm5oWj5piw442m45Sy45mk5oiz44i357S3";
if(!empty($flag)){
    $xx = mb_list_encodings(); 
    $flag = base64_decode($flag);
    $xx = array("1337" => $xx[3]);
    $flag = mb_convert_encoding($flag, $xx['1337'], 'UTF-8' );
    echo "<h1>The baby encoder!</h1>
    Your encoded flag is <strong>$flag</strong>";
} else {
    die("Missing parameters!");
}
