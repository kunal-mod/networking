import struct
from PIL import Image
import pyshark
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

capture = pyshark.LiveCapture(
    interface="Adapter for loopback traffic capture", bpf_filter="host 127.0.0.1 and port 8500")
# capture.sniff(timeout=0.1)
display_filter = 'tcp'
image_data = b''
flag = 0
for packet in capture.sniff_continuously():
    if display_filter in packet:
        if (str(packet.ip.src) == "127.0.0.1" and str(packet.tcp.srcport) == "8500"):
            x = int(packet.tcp.len)
            if (x > 800):
                print(x)
                field_names = list(packet.tcp._all_fields)
                field_values = list(packet.tcp._all_fields.values())
                for i in range(len(field_names)):
                    if (str(field_names[i]) == "tcp.payload"):
                        if (x > 800 and x < 1000):
                            print(f'{field_names[i]} -- {field_values[i]}')
                        hex_code = str(field_values[i])
                        byte_obj = bytes.fromhex(hex_code.replace(':', ''))
                        # print(byte_obj.decode('utf-8'))
                        image_data += byte_obj
                flag += 1
            print(flag)
            if (flag == 482):
                print("till 810")
                break
            tcp_layer = packet['TCP']
            if (tcp_layer.flags_fin == '1'):
                print("fin flag recieved")
                break
with open('aagai_img.bin', 'wb') as f:
    f.write(image_data)


with open('aagai_img.bin', 'rb') as f:
    pixel_data = f.read()
width = 1600
height = 1200
image = Image.frombytes('L', (width, height), pixel_data)
image.save('image.png')
image.show()


# print("Outside")
# # Display the image
# img = mpimg.imread('aagai_img.bmp')
# plt.imshow(img)
# plt.show()

print("Exit")
