import socket
import ssl
import requests

host_addr = '127.0.0.1'
host_port = 443
server_sni_hostname = 'example.com'
server_cert = './certificates/server.pem'  #to validate


context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_verify_locations(cafile=server_cert)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn = context.wrap_socket(s, server_side=False, server_hostname=server_sni_hostname)
conn.connect((host_addr, host_port))
print("SSL established. Peer: {}".format(conn.getpeercert()))


print("Sending message")
conn.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
print("sent") 

try:	
	print("recieve response:")
	response = conn.recv(4096)
	print(response)   

except:
    pass


print("Closing connection")
conn.close()