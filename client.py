import socket, argparse
from server import Server
import time

class Client(Server):#inherits from the Server class
    #initializes the client connection to the server on the specified address
    def __init__(self, address,port):
        print("in the client")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((address,port))

        
    def return_socket(self):
        return self.sock
    
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("ip")

    parser.add_argument("--port", default=1060)

    args = parser.parse_args()
    newclient = Client(args.ip,args.port)
    clientsock = newclient.return_socket()
    msg = "Hi there server"+'?'
    
 
    msg = msg.encode('ascii')
    clientsock.sendall(msg)
   
    while True:

        newmessage=newclient.recv_msg(clientsock,b'?')
        print("The server sent back \n"+newmessage.decode('ascii'))

    print("after loop")
