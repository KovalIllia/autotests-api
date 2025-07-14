from typing import TypedDict
from httpx import Response

from clients.api_client import APIClient


class LoginRequestDict(TypedDict):
    """Description of the authentication request structure."""
    email: str
    password:str


class RefreshRequestDict(TypedDict):
    """Description of the structure of the request for updating the token."""
    refreshToken: str#in general Python named like snake_case, buy this camelCase



class AuthenticationClient(APIClient):
    """Client for working with /api/v1/authentication"""
    pass

    def login_api(self, request: LoginRequestDict) -> Response:
        """The method authenticates the user.
        :param request: Dictionary with email and password.
        :return: Response from the server as an httpx.Response object"""
        return self.post("/api/v1/authentication/login", json=request)

# 
# client=AuthenticationClient()
# client.login_api({'email':'k@mail.com','paswod': 'sss'})

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """The method refreshes the authorization token.
        :param request: Dictionary with refreshToken.
        :return: Response from the server as an httpx.Response object
        """
        return self.post("/api/v1/authentication/refresh", json=request)