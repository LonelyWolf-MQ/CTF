#!/bin/bash

openssl enc -d -aes-256-cbc -in secret.txt.enc -out flag.txt -k 123 -pbkdf2 

echo  "secret.txt created as decrypted file"
