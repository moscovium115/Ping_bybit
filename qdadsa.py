import ast
import socket
import ssl
from time import time_ns

# Define the target host and port
HOST = 'api.bybit.com'
PORT = 443

# Define the API endpoint
ENDPOINT = '/v5/market/time'

# Define the HTTP request
request = f"GET {ENDPOINT} HTTP/1.1\r\nHost: {HOST}\r\n\r\n"

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrap the socket with SSL/TLS
context = ssl.create_default_context()
ssl_sock = context.wrap_socket(sock, server_hostname=HOST)

# Enable TCP_NODELAY option
ssl_sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

# Connect to the server
ssl_sock.connect((HOST, PORT))

# Send the HTTP request
time_1=time_ns()
ssl_sock.sendall(request.encode())

# Receive the response
response = b""

chunk = ssl_sock.recv(4096)
time_2=time_ns()
# format as json
response_1=str(chunk.decode())
print(response_1)
# response= ast.literal_eval(response)
#reponse turn str to dict
# response=eval(response)

# Extracting the JSON part of the response
json_start_index = response_1.find('{')
json_end_index = response_1.rfind('}') + 1
json_string = response_1[json_start_index:json_end_index]

# Convert the JSON string to a dictionary
import json
response_dict = json.loads(json_string)

# Extract the "timeNano" value from the dictionary
time_nano = int(response_dict['result']['timeNano'])
print("time_1:",time_1)
print("time_2:",time_2)
print("timeNano:",time_nano)
print("time diff nano",time_nano-time_1)
print("time diff time nano",(time_nano-time_1)/1e6)
print("Time taken to receive response:", (time_2-time_1)/1e6)



# Print the response
# print(response.decode())

# Close the socket
ssl_sock.close()
