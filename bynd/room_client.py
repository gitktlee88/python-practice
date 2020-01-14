# Python program to implement client side of chat room.
# import socket
# import select
# import sys
#
# c_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# if len(sys.argv) != 3:
#     print ("Correct usage: script, IP address, port number")
#     exit()
# IP_address = str(sys.argv[1])
# Port = int(sys.argv[2])
# c_sock.connect((IP_address, Port))
#
# while True:
#
#     # maintains a list of possible input streams
#     #sockets_list = [sys.stdin, c_sock]
#     sockets_list = [socket.socket(), c_sock]
#     #print(sockets_list)
#
#     """ There are two possible input situations. Either the
#     user wants to give  manual input to send to other people,
#     or the server is sending a message  to be printed on the
#     screen. Select returns from sockets_list, the stream that
#     is reader for input. So for example, if the server wants
#     to send a message, then the if condition will hold true
#     below.If the user wants to send a message, the else
#     condition will evaluate as true"""
#     read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
#
#     for socks in read_sockets:
#         if socks == c_sock:
#             message = socks.recv(2048)
#             print (message)
#         else:
#             message = sys.stdin.readline()
#             c_sock.send(message)
#             sys.stdout.write("<You>")
#             sys.stdout.write(message)
#             sys.stdout.flush()
# c_sock.close()

import socket, select, string, sys, time, msvcrt

def prompt() :
    sys.stdout.write('\n<You> ')
    sys.stdout.flush()

def input_with_timeout_windows(prompt, timeout, default):
    start_time = time.time()
    print (prompt)
    sys.stdout.flush()
    input = ''
    while True:
        if msvcrt.kbhit():
            chr = msvcrt.getche().decode('utf-8')
            if ord(chr) == 13: # enter_key
                break
            elif ord(chr) >= 32: #space_char
                input += chr
        if len(input) == 0 and (time.time() - start_time) > timeout:
            break
    if len(input) > 0:
        return input
    else:
        return default


#main function
if __name__ == "__main__":

    if(len(sys.argv) < 3) :
        print ('Usage : python telnet.py hostname port')
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

    print ('Connected to remote host. Start sending messages')
    prompt()

    while 1:
        #socket_list = [sys.stdin, s]
        socket_list = [s]
        #print(socket_list)

        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [], 1)
        if msvcrt.kbhit(): read_sockets.append(sys.stdin)
        #print(read_sockets, file=sys.stderr)

        for sock in read_sockets:
            if sock == s:
                # incoming message from remote server, s
                data = sock.recv(4096)
                if not data :
                    print ('\nDisconnected from chat server')
                    sys.exit()
                else :
                    #print data
                    sys.stdout.write(data.decode('utf-8'))
                    sys.stdout.write('\n[Me] '); sys.stdout.flush()

            else :
                # user entered a message
                msg = sys.stdin.readline()
                #msg = input_with_timeout_windows('>', 3, 'default')
                s.send(msg.encode('utf-8'))
                sys.stdout.write('[Me] '); sys.stdout.flush()
