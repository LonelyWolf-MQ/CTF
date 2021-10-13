## To solve the challenge, lets understand the code.


### The code will wait for a get request with parameter named as flag, otherwise it will print "Missing Parameter".
`$flag = $_GET['flag'] ?? null;`


### Here it will list all the encoding within php to $xx variable.
`$xx = mb_list_encodings();`
#### Note: you can get all encodings in this function by executing `print_r($xx);`


### Then it will assign a name "1337" to the fourth array which is "byte2be" encoding.
`$xx = array("1337" => $xx[3]);`


### Here it will use this function to encode the flag variable from "byte2be" to "UTF-8".
`$flag = mb_convert_encoding($flag, 'UTF-8', $xx["1337"]);`


### lastly it will encode the value with base64 encoding.
`$flag = base64_encode($flag);`


### so let us solve this challenge by doing the reverse of the encoding method.
- encoding method ( byte2be => UTF-8 => base64).
- decoding method ( base64 => UTF-8 => byte2be).


## And then will have the flag.
`IAUflag{20f4b92b64b972bfbca0ff325d63b727}`
