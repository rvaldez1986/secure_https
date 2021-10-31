import socket
#from socket import AF_INET, SOCK_STREAM, SO_REUSEADDR, SOL_SOCKET, SHUT_RDWR
import ssl

listen_addr = '127.0.0.1'
listen_port = 80
server_cert = 'server.crt'
server_key = 'server.key'

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile=server_cert, keyfile=server_key)

bindsocket = socket.socket()
bindsocket.bind((listen_addr, listen_port))
bindsocket.listen(5)

def handle(data, conn):
    rec = repr(data)
    print("Received:", rec)
    #Check if GET request

    response = b'<html><body><h1>Get Request Received!</h1></body></html>'
    conn.send(response)
    



while True:
    print("Waiting for a client to connect")
    newsocket, fromaddr = bindsocket.accept()
    print("Client connected: {}:{}".format(fromaddr[0], fromaddr[1]))
    conn = context.wrap_socket(newsocket, server_side=True)
    print("SSL established")
    try:
        data = conn.recv(4096)
        handle(data, conn)               
            
    except:
        #connection was closed
        if data:
            #we received data
            pass
        else:
            print("something went wrong")
            break
        
    finally:
        print("Closing connection")
        try:
            conn.shutdown(socket.SHUT_RDWR)
        except socket.error:
            pass  # Ignore if the socket is already down        
        conn.close()