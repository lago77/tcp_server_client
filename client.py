import socket, argparse
from server import Server

class Client(Server):#inherits from the Server class
    #initializes the client connection to the server on the specified address
    def __init__(self, address,port):
        print("in the client")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((address,port))
        msg = "Hi there server"+'?'
        msg = msg.encode('ascii')
        self.sock.sendall(msg)
        while True:
            mymessage = self.recv_msg(self.sock,b'?')
            print(mymessage)
        

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("ip")

    parser.add_argument("--port", default=1060)

    args = parser.parse_args()
    newclient = Client(args.ip,args.port)
