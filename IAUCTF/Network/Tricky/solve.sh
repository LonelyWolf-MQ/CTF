#!/bin/bash

foremost Tricky.pcap
cd output/png
mogrify -negate *.png
zbarimg -q *.png | sed 's/QR-Code://g' | tr -d '\n' > base64
sed 's/SAK//' base64 | base64 -d | grep 'IAU'
