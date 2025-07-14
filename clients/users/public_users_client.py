from typing import TypedDict
from httpx import Response

from clients.api_client import APIClient


class UserCreationRequestDict(TypedDict):
    """Description of the authentication request structure."""
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    """Client for working with /api/v1/users -- creation new user"""


    def create_user_api(self, request: UserCreationRequestDict) -> Response:
        """The method for creating new user.
        :param request: Dictionary with email,passwor,lastName,fistName,middleName
        :return: Response from the server as an httpx.Response object"""
        return self.post("/api/v1/users", json=request)
