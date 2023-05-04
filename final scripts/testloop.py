import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('10.166.76.39', 8500)
s.connect(server_address)


def printHex(data):
    print(' '.join('{:02x}'.format(x) for x in data))


def sendCommand(cmd):
    command = bytes.fromhex(cmd)
    s.send(command)
    data = s.recv(1024)                         # response 00 04 00 00
    printHex(data)


def querySuccess():
    command = bytes.fromhex('00 05 f0 15 e0')
    s.send(command)
    # response 00 08 00 00 00 00 00 08
    data = s.recv(1024)
    printHex(data)


def communicationSetup():
    # to initiate connection
    sendCommand('00 04 fd f9')
    # to set Acq, Work, Demo and Display page
    sendCommand('00 09 05 ff 00 00 00 00 f3')
    querySuccess()


def setOut1High():
    sendCommand('00 08 41 10 00 01 01 59')
    querySuccess()


def setOut2High():
    sendCommand('00 08 41 10 01 01 01 58')
    querySuccess()


def setOut2Low():
    sendCommand('00 08 41 10 01 00 01 59')
    querySuccess()


def setOut3Low():
    sendCommand('00 08 41 10 02 00 01 5a')
    querySuccess()


def setOut4Low():
    sendCommand('00 08 41 10 03 00 01 5b')
    querySuccess()


def setOut3High():
    sendCommand('00 08 41 10 02 01 01 5b')
    querySuccess()


def setOut4High():
    sendCommand('00 08 41 10 03 01 01 5a')
    querySuccess()


def queryIN1High():
    sendCommand('00 08 41 60 00 01 01 29')
    querySuccess()
    # if success IN_1HIGH = 1 else 0


def queryIN1Low():
    sendCommand('00 08 41 60 00 00 01 28')
    querySuccess()
    # if success IN_1LOW = 1 else 0


def doneAndWait():
    setOut1High()
    setOut2Low()
    IN_1HIGH = 1
    while (IN_1HIGH == 1):
        queryIN1High()


def triggerStart():
    IN_1LOW = 1
    while (IN_1LOW == 1):
        queryIN1Low()


def activateSystem():
    setOut2High()
    setOut3Low()
    setOut4Low()


def setExposure():
    sendCommand('00 0b 07 00 04 00 01 86 a0 00 2f')
    querySuccess()


def captureImage():
    pass


def doImageProcessing():
    pass


def partOK():
    setOut3High()
    setOut2Low()


def partNOK():
    setOut4High()
    setOut2Low()


def mainloop():
    setExposure()
    captureImage()
    result = doImageProcessing()
    if (result == True):
        partOK()
    else:
        partNOK()


if __name__ == "__main__":

    communicationSetup()

    while True:
        doneAndWait()
        triggerStart()
        activateSystem()
        mainloop()
