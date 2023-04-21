import socket
import time
import struct


def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
    return get_mac_address(dest_mac), get_mac_address(src_mac), socket.htons(proto), data[14:]


def get_mac_address(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    return (":".join(bytes_str).upper())


def main():
    conn = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    conn.bind(("127.0.0.1", 0))
    conn.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    conn.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    packet, addr = conn.recvfrom(65565)
    # Extract the IP header using struct
    ip_header = packet[0:20]
    iph = struct.unpack('!BBHHHBBH4s4s', ip_header)

    # Get the source and destination IP addresses from the header
    source_address = socket.inet_ntoa(iph[8])
    destination_address = socket.inet_ntoa(iph[9])

    # Print the source and destination IP addresses

    # Print the complete IP header in human-readable format
    print("IP Header:")
    print("  Version:", (iph[0] >> 4))
    print("  Header Length:", (iph[0] & 0xF) * 4)
    print("  Type of Service:", iph[1])
    print("  Total Length:", iph[2])
    print("  Identification:", iph[3])
    print("  Flags:", (iph[4] >> 13))
    print("  Fragment Offset:", (iph[4] & 0x1FFF))
    print("  Time to Live:", iph[5])
    print("  Protocol:", iph[6])
    print("  Header Checksum:", iph[7])
    print("  Source Address:", str(source_address))
    print("  Destination Address:", str(destination_address))

    tcp_header = packet[20:40]
    tcph = struct.unpack('!HHLLBBHHH', tcp_header)

    # Print the TCP header fields
    print("TCP Header:")
    print("  Source Port:", tcph[0])
    print("  Destination Port:", tcph[1])
    print("  Sequence Number:", tcph[2])
    print("  Acknowledgement Number:", tcph[3])
    print("  Header Length:", (tcph[4] >> 4) * 4)
    print("  Flags:", tcph[5])
    print("  Window Size:", tcph[6])
    print("  Checksum:", tcph[7])
    print("  Urgent Pointer:", tcph[8])

    conn.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

# hex_string = "0007a01aff0042"
# byte_string = bytes.fromhex(hex_string)
# s.send(byte_string)
# time.sleep(1)

# msg = s.recvfrom(1024)
# print(msg.decode("utf-8"))
# s.close()
# print('Connection closed.')


main()
