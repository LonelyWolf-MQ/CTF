from scapy.all import *
import base64

packet = rdpcap('ARP+Storm.pcap')
lis = []
for p in packet:
	a = p.show(dump=True)
	op = p.op
	lis.append(chr(op))
b64 = ''.join(lis)
de = base64.b64decode(b64)
print('flag is: ' + de.decode('utf-8'))
