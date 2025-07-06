import socket  # Import the socket module to work with network connections


def server():
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # add the connection to the created TCP socket and to the address and port
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # We start listening to incoming connections (maximum 5 in a queue)
    server_socket.listen(5)
    print("The server is running and waiting the new connections...")

    while True:
        # We accept the connection from the client
        client_socket, client_address = server_socket.accept()
        print(f"Connection from  {client_address}")

        # We receive data from the client
        data = client_socket.recv(1024).decode()
        print(f"Received the message : {data}")

        # send a response to the client
        response = f"The server received: {data}"
        client_socket.send(response.encode())

        # close the connection with the client
        client_socket.close()


if __name__ == '__main__':
    server()
