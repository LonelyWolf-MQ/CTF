As the challenge name, we will think about destination.
First, we will see two protocols in the pcap (ICMP,TCP), we will notice that ICMP protocol has no information
So if we start to search with TCP we will see it tries to perform a TCP Syn Scan but the number of ports are abnormal
If we filter (tcp.flags.syn==1)
