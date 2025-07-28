from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.users.private_users_client import PrivateUsersClient

class File(TypedDict):
    """Description of file structure"""
    id: str
    filename: str
    directory: str
    url: str

class CreateFileRequestDict(TypedDict):
    """Description of the structure of a file creation request."""
    filename: str
    directory: str
    upload_file: str

class CreateFileResponseDict(TypedDict):
    """Description of the structure of the file creation response."""
    file: File



class FilesClient(APIClient):
    """Client for working with /api/v1/files"""

    def get_file_api(self, file_id: str) -> Response:
        """Method for getting a file.
        :param file_id: File identifier.
        :return: Response from the server as an httpx.Response object"""
        return self.get(f"/api/v1/files/{file_id}")

    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        """Method for creating a file.
        :param request: Dictionary with filename, directory, upload_file.
        :return: Response from the server as an httpx.Response object"""
        return self.post(f"/api/v1/files", data=request,
                         files={"upload_file": open(request["upload_file"], 'rb')})

    def delete_file_api(self, file_id: str) -> Response:
        """Method for deleting a file.
        :param file_id: File identifier.
        :return: Response from the server as an httpx.Response object"""
        return self.delete(f"/api/v1/files/{file_id}")

    def create_file(self,request: CreateFileRequestDict)-> CreateFileResponseDict:
        response=self.create_file_api(request)
        return response.json()




def get_files_client(user: AuthenticationUserSchema) -> FilesClient:
    """The function creates a FilesClient instance with the HTTP client already configured.
    :return: The FilesClient is ready to use."""
    return FilesClient(client=get_private_http_client(user))

# client=get_private_users_client({"email": "ssd@", "password": "sdsdsd"})
# client.delete() #logined user