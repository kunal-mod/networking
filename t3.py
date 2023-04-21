import pyshark

capture = pyshark.LiveCapture()
# capture.sniff(timeout=0.1)
display_filter = 'tcp'
for packet in capture.sniff_continuously():
    if display_filter in packet:
        if (str(packet.ip.src) == "127.0.0.1" and str(packet.tcp.srcport) == "1234"):

            # src_ip = packet.ip.src
            # dst_ip = packet.ip.dst
            # src_port = packet.tcp.srcport
            # dst_port = packet.tcp.dstport
            # print(f'Source IP: {src_ip}')
            # print(f'Destination IP: {dst_ip}')
            # print(f'Source Port: {src_port}')
            # print(f'Destination Port: {dst_port}')

            field_names = list(packet.tcp._all_fields)
            field_values = list(packet.tcp._all_fields.values())
            for i in range(len(field_names)):
                if (str(field_names[i]) == "tcp.payload"):
                    hex_code = str(field_values[i])
                    byte_obj = bytes.fromhex(hex_code.replace(':', ''))
                    print(byte_obj.decode('utf-8'))
