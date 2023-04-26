import time
from scapy.all import *
from scapy.layers.inet import TCP, IP

# Set the server IP address and port number
server_ip = '127.0.0.1'
server_port = 8500

# Set the client IP address and port number
client_ip = '127.0.0.1'
client_port = 53962

# Create the message payload in hex format
payload = Raw(b'\x00\x08\x41\x00\x01\x01\x59')

# Create a custom packet with the desired source IP and port
packet = IP(src=client_ip, dst=server_ip) / \
    TCP(sport=client_port, dport=server_port)/payload

# Send the packet to the server
send(packet)
time.sleep(0.2)
send(packet)
