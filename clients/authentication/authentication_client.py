from typing import TypedDict
from httpx import Response, Client

from clients.api_client import APIClient
from clients.public_http_builder import  get_public_http_client

class LoginRequestDict(TypedDict):
    """Description of the authentication request structure."""
    email: str
    password:str


class RefreshRequestDict(TypedDict):
    """Description of the structure of the request for updating the token."""
    refreshToken: str #in general Python named like snake_case, buy this camelCase



class AuthenticationClient(APIClient):
    """Client for working with /api/v1/authentication"""


    def login_api(self, request: LoginRequestDict) -> Response:
        """The method authenticates the user.
        :param request: Dictionary with email and password.
        :return: Response from the server as httpx.Response object"""
        return self.post("/api/v1/authentication/login", json=request)

# 
# client=AuthenticationClient()
# client.login_api({'email':'k@mail.com','paswod': 'sss'})

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """The method refreshes the authorization token.
        :param request: Dictionary with refreshToken.
        :return: Response from the server as httpx.Response object
        """
        return self.post("/api/v1/authentication/refresh", json=request)


def get_authentication_client()-> AuthenticationClient:
    """The function creates an instance of AuthenticationClient with the HTTP client already configured.
        :return: A ready-to-use AuthenticationClient."""
    # return AuthenticationClient(client=Client(timeout=100,base_url="http://localhost:8000")) #analog
    return AuthenticationClient(client=get_public_http_client())

#
# test_client=get_authentication_client()
# test_client.