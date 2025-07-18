from typing import TypedDict
from httpx import Response,Client

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client


class User(TypedDict):
    """Description of the user structure."""
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class CreateUserRequestDict(TypedDict):
    """Description of the authentication request structure."""
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class CreateUserResponseDict(TypedDict):
    """Description of the structure of the user creation response."""
    user: User

class PublicUsersClient(APIClient):
    """Client for working with /api/v1/users -- creation new user"""


    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """The method for creating new user.
        :param request: Dictionary with email,passwor,lastName,fistName,middleName
        :return: Response from the server as httpx.Response object"""
        return self.post("/api/v1/users", json=request)

    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict:
        response = self.create_user_api(request)
        return response.json()

def get_public_users_client()-> PublicUsersClient:
    """The function creates an instance of PublicUsersClient with the HTTP client already configured.
        :return: Ready-to-use PublicUsersClient."""
    # return AuthenticationClient(client=Client(timeout=100,base_url="http://localhost:8000")) #analog
    return PublicUsersClient(client=get_public_http_client())


#   analog-> without builder
#   httpx_client=Client(timeout=100,base_url="http://localhost:8000")
#   client=PublicUsersClient(client=httpx_client)
#   client.create_user_api()

#   with builder
#   client=get_public_users_client()
#   client.create_user_api()