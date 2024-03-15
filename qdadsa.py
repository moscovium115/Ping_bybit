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
while True:
    chunk = ssl_sock.recv(4096)
    time_2=time_ns()
    print(chunk)
    print("Time taken to receive response:", (time_2-time_1)/10e6)
    if not chunk:
        break
    response += chunk

# Print the response
print(response.decode())

# Close the socket
ssl_sock.close()
