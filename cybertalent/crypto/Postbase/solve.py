import base64
import re

b64 = 'R$$BR3tCNDUzXzYxWDdZXzRSfQ=='
lenb64 = len(b64)
cob64 = b64.count('$')
if (lenb64 % 4) == 0 and cob64 == 0:
    deb64 = base64.b64decode(b64)
    print(deb64)
else:
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    for i in letters:
        sub = b64.replace('$',i,1)
        for j in letters:
            sub1 = sub.replace('$',j,1)
            deb64 = base64.b64decode(sub1)    
            s = re.findall('FLAG{', str(deb64))
            if s:
                print("Challenge Flag is: "+deb64.decode('utf-8'))
