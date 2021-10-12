import os
import hashlib
import base64
os.system("tshark -r test.pcapng --export-objects http,. > /dev/null 2>&1")
with open('data.txt','r') as f:
    lines = f.readline()
decode = base64.b32decode(lines)
with open('flag.jpeg' ,'wb') as f :
	f.write(decode)
with open("flag.jpeg", "rb") as f:
	file_hash = hashlib.md5()
	while chunk := f.read(8192):
		file_hash.update(chunk)
print("Flag is:  IAUflag{"+file_hash.hexdigest()+"}")
