from scapy.all import *
import base64
packet = rdpcap('destiny.pcap')
b64 = ""
for p in packet:
	if p.haslayer(TCP):
		if p[TCP].seq != 0:
			d = p[TCP].dport
			b64 += chr(d)
decode = base64.b64decode(b64)
print('flag is: ' + decode.decode('utf-8'))
