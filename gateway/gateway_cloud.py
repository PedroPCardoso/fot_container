import socket
from threading import Thread
from SocketServer import ThreadingMixIn
import json
import heapq

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread):
    global list_devices
    global size_list_devices
    size_list_devices = 3
    list_devices = {}
    def __init__(self,ip,port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        list_devices = {}    
        print "[+] New server socket thread started for " + ip + ":" + str(port)

    def run(self):
        while True :
            global size_list_devices
            global list_devices
            data = conn.recv(2048)
            loaded_r = json.loads(data)
            print "LISTA"
            print loaded_r
            print "END LISTA"
            kvalues = heapq._nlargest(2,loaded_r.values())
            print "Server received data:", kvalues
            if len(list_devices.values()) == size_list_devices:
                #transformar em json para enviar
                data = json.dumps(list_devices)
                print "enviadooooooooooooooooooooooooo" +  data
                self.send_cloud(data)
                list_devices = {}
            else:
                #add dentro do dicionario
                name =  "g"+str(len(list_devices.values()))
                list_devices[name] = kvalues
            MESSAGE = raw_input("Multithreaded Python server : Enter Response from Server/Enter exit:")
            if MESSAGE == 'exit':
                break
    def send_cloud(self,msg):
        sock_cloud = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cloud_address = ('localhost', 2004)
        sock_cloud.connect(cloud_address)
        sock_cloud.sendall(msg)

# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = '0.0.0.0'
TCP_PORT = 20001
BUFFER_SIZE = 20  # Usually 1024, but we need quick response

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpServer.listen(4)
    print "Multithreaded Python server : Waiting for connections from TCP clients..."
    (conn, (ip,port)) = tcpServer.accept()
    newthread = ClientThread(ip,port)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()
