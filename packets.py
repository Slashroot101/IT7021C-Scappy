from scapy.all import *

for n in range(10):
	srcIP="172.16.16."+str(RandNum(1, 254))
	destIP="192.168.5.5"
	ipFlags=0 if((n+1)%5) else 4
	payload="Bad" if((n+1)%2) else "Good"
	ip=IP(src=srcIP, flags=ipFlags, dst=destIP, ttl=160)
	tcpFlag = 'S' if((n+1) < 5) else 'FU'
	send(ip/TCP(dport=RandNum(1000, 1009), flags=tcpFlag))