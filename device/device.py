import socket
import sys
import random
import heapq
import time
import json
for i in range(0,3):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 20001)
    print >>sys.stderr, 'connecting to %s port %s' % server_address
    sock.connect(server_address)
    list_devices ={}
    try:
        k=2;
        # Send data
        for a in range(0,50):
            if i == 0:
                info = random.randint(10,13)
                devic = 'j' + str(a)
                list_devices[devic] = info
            if i == 1:
                info = random.randint(10,17)
                devic = 'j' + str(a)
                list_devices[devic] = info
            if i == 2:
                info = random.randint(10,20)
                devic = 'j' + str(a)
                list_devices[devic] = info
        r = json.dumps(list_devices)
        loaded_r = json.loads(r)
        sock.sendall(r)
    finally:
        print >>sys.stderr, 'closing socket'
        sock.close()
