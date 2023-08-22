
import argparse, socket, time

class Server():
    #initializes a server instance and binds it to the host network ip
    def __init__(self, address, port):
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listener.bind((address,1060))
        self.listener.listen()
        print('Listening at {}'.format(self.listener.getsockname()))
        #return self.listener
        #self.serve(self.listener)
    def ret_listener(self):
        return self.listener
    ### passes the listening socket to accept incoming connections and creates a new active socket from a client connection
    def serve(self,listener):
        while True:
            sock, address = listener.accept()
            print("Connection from {} has been accepted".format(address))
            self.handler(sock)

    ### method to repeatedly listen for communication
    def handler(self, sock):
        try:
            while True:
                self.comm(sock)
        except EOFError:
            print('Client socket has closed')
        except Exception as e:
            print("Client error {}".format(e))
        finally:
            sock.close()
    ###method to receive communication a peer then to send it back. 
    def comm(self,sock):
        clientmsg = self.recv_msg(sock,b'?')
        sendback = "This is what you sent: "+clientmsg.decode('ascii')
        sock.sendall(sendback.encode('ascii'))
      

    ### method that waits to receive data until it's finished sending via the use of a delimiter
    def recv_msg(self,sock,delim):
  
        message = sock.recv(4096)

        if not message:
             raise EOFError("Error: Socket closed")
        while not message.endswith(delim):
            data = sock.recv(4096)
            print("in not message")
            print(type(message))
            if not data:
                raise IOError('IO error for the message sent'.format(message))
            message += data
        return message
