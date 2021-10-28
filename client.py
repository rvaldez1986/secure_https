import requests
import ssl

server_address = 'http://127.0.0.1'

response = requests.get(server_address, verify = True)
print("send a get requrest to", server_address)

print(response.status_code, response.reason)
if response:
    print('Success!')
else:
    print('An error has occurred.')

