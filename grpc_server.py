from concurrent import futures  # Importing a thread pool for asynchronous execution

import grpc  # Importing the gRPC library

import user_service_pb2  # Generated classes for working with gRPC messages
import user_service_pb2_grpc  # Generated class for working with the service


# Implementing a gRPC service
class UserServiceServicer(user_service_pb2_grpc.UserServiceServicer):
    """Implementing gRPC service methods for UserService"""

    def GetUser(self, request, context):
        """Method GetUser processes an incoming request"""
        print(f'A request was received for the GetUser method from a user: {request.username}')

        # generate and return a response message
        return user_service_pb2.GetUserResponse(message=f"Hello, {request.username}!")


# Function to start gRPC server
def serve():
    """The function creates and starts a gRPC server."""

    # Create a server using a thread pool (up to 10 threads)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Registering the UserService service on the server
    user_service_pb2_grpc.add_UserServiceServicer_to_server(UserServiceServicer(), server)

    # Configure the server to listen on port 50051
    server.add_insecure_port('[::]:50051')

    # Launching the server
    server.start()
    print("gRPC server running on port 50051...")

    # Waiting for the server to complete its work
    server.wait_for_termination()


# Starting the server when executing a script
if __name__ == "__main__":
    serve()
