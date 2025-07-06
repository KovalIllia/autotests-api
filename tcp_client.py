import socket

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting to the server
server_address = ('localhost', 12345)
client_socket.connect(server_address)

# Sending a message to the server
message = "Hello, TCP server!"
client_socket.send(message.encode())

# We receive a response from the server
response = client_socket.recv(1024).decode()
print(f"Response from the server: {response}")

# Closing the connection
client_socket.close()
