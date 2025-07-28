from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client


class User(TypedDict):
    """Description of the user structure."""
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class UpdateUserRequestDict(TypedDict):
    """Description of the structure of a user update request."""
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None


class GetUserResponseDict:
    """Description of the structure of the user's response."""
    user: User


class PrivateUsersClient(APIClient):
    """Client for working with /api/v1/users"""

    def get_user_me_api(self) -> Response:
        """Method for getting the current user.
        :return: Response from the server as an httpx.Response object"""
        return self.get("/api/v1/users/me")

    def get_user_api(self, user_id: str) -> Response:
        """Method for getting user by ID.
        :param user_id: User ID.
        :return: Response from server as httpx.Response object"""
        return self.get(f"/api/v1/users/{user_id}")

    def update_user_api(self, user_id: str, request: UpdateUserRequestDict) -> Response:
        """Method for updating a user by ID.
        :param user_id: User ID.
        :param request: Dictionary with email, lastName, firstName, middleName.
        :return: Response from the server as an httpx.Response object."""
        return self.patch(f"/api/v1/users/{user_id}", json=request)

    def delete_user_api(self, user_id: str) -> Response:
        """ Method for deleting a user by ID.
        :param user_id: User ID.
        :return: Response from the server as an httpx.Response object"""
        return self.delete(f"/api/v1/users/{user_id}")

# print(UpdateUserRequestDict().get("email"))
# print(UpdateUserRequestDict().get("email", "sdsdsdsds"))

    def get_user(self, user_id: str) -> GetUserResponseDict:
        response = self.get_user_api(user_id)
        return response.json()


def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    """The function creates an instance of PrivateUsersClient with the HTTP client already configured.
    :return: Ready-to-use PrivateUsersClient."""
    return PrivateUsersClient(client=get_private_http_client(user))

# client=get_private_users_client({"email": "ssd@", "password": "sdsdsd"})
# client.delete() #logined user