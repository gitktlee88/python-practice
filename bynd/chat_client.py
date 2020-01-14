# chat_client.py
"""
This chat client is not going to work on windows.
It uses the select function to read data from both the socket and the input stream.
This works on linux but not on windows.

The python documentation on select mentions this:
Linux treats sockets and file descriptors in the same manner, therefore
    the select function is able to read from stdin.
On windows the select function will not read anything
    except sockets created by the winsock socket functions.
"""
import sys
import socket
import select

##############################################
from threading import *
def send_msg(sock):
    while True:
        data = sys.stdin.readline()
        #sock.sendto(data, target)
        sock.send(str.encode(data, 'utf-8'))
        sys.stdout.write('[Me] '); sys.stdout.flush()

# def recv_msg(sock):
#     while True:
#         data, addr = sock.recvfrom(1024)
#         sys.stdout.write(data); sys.stdout.flush()

#############################################

def chat_client():
    if(len(sys.argv) < 3) :
        print ('Usage : python chat_client.py hostname port')
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print ('Unable to connect')
        sys.exit()

    print ('Connected to remote host. You can start sending messages')
    sys.stdout.write('[Me] '); sys.stdout.flush()

    #temporary solution fixing select error on windows.
    Thread(target=send_msg, args=(s,)).start()
    #Thread(target=recv_msg, args=(s,)).start()

    while 1:
        #socket_list = [sys.stdin, s]
        socket_list = [socket.socket(), s]

        # Get the list sockets which are readable
        ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])

        for sock in ready_to_read:
            if sock == s:
                # incoming message from remote server, s
                data = sock.recv(4096)
                if not data :
                    print ('\nDisconnected from chat server')
                    sys.exit()
                else :
                    sys.stdout.write(data)
                    sys.stdout.write('[Me] '); sys.stdout.flush()

            else :
                # user entered a message
                #msg = sys.stdin.readline()
                msg = socket.socket().readline()
                s.send(msg)
                sys.stdout.write('[Me] '); sys.stdout.flush()

if __name__ == "__main__":

    sys.exit(chat_client())
