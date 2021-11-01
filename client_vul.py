import requests
import ssl

server_address = 'https://www.google.com'

query = "cat"

query = {'q': query}

response = requests.get(server_address, verify=False, params=query)
print("send a get requrest to", server_address)

print(response.status_code, response.reason)
print(response)
if response:
    print('Success!')
else:
    print('An error has occurred.')

