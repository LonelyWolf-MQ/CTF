from scapy.all import *
import codecs
packet = rdpcap('Packet-abomination.pcap')
pcts = []
b = ""
for p in packet:
    if p.haslayer(DNS):
        a = p.show(dump=True)
        if 'load' in a:
            data = p[DNS].load
            pcts.append(codecs.encode(data,'hex').decode('utf-8'))
        else:
            continue    
for i in sorted(pcts):
	i = i[-2:]
	b += i
tohex = codecs.decode(b,"hex")
print("flag is: "+ tohex.decode("utf-8"))
