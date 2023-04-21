import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 1234))

for i in range(2):
    s.send(bytes("open", "utf-8"))
    msg = s.recv(1024)
    print(msg.decode("utf-8"))
    # decimal_list = list(msg)
    # binary_list = [bin(decimal)[2:].zfill(8) for decimal in decimal_list]
    # bits_string = ' '.join(binary_list)
    # print(bits_string)
    # time.sleep(1)

s.send(bytes("close", "utf-8"))
s.close()
print('Connection closed.')
