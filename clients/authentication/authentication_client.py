from typing import TypedDict
from httpx import Response, Client

from clients.api_client import APIClient
from clients.public_http_builder import  get_public_http_client

from clients.authentication.authentication_schema import TokenSchema,LoginRequestSchema,LoginResponceSchema,RefreshRequestSchema
# from grpc_client import response

#in lesson 7.2 p1 was replaced TypedDict replaced with a new Pydantic scheme
# class Token(TypedDict):
#     """Added structure with authentication tokens"""
#     token_type: str
#     access_token: str
#     refresh_token: str
#
#
# class LoginRequestDict(TypedDict):
#     """Description of the authentication request structure."""
#     email: str
#     password:str
#
# class LoginResponceDict(TypedDict):
#     """Description of the structure of the authentication response"""
#     token:Token
#
#
#
# class RefreshRequestDict(TypedDict):
#     """Description of the structure of the request for updating the token."""
#     refreshToken: str #in general Python named like snake_case, buy this camelCase



class AuthenticationClient(APIClient):
    """Client for working with /api/v1/authentication"""


    def login_api(self, request: LoginRequestSchema) -> Response:
        """The method authenticates the user.
        :param request: Dictionary with email and password.
        :return: Response from the server as httpx.Response object"""
        return self.post("/api/v1/authentication/login", json=request.model_dump(by_alias=True))

# 
# client=AuthenticationClient()
# client.login_api({'email':'k@mail.com','paswod': 'sss'})

    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        """The method refreshes the authorization token.
        :param request: Dictionary with refreshToken.
        :return: Response from the server as httpx.Response object
        """
        return self.post("/api/v1/authentication/refresh", json=request.model_dump(by_alias=True))

    def login(self,request:LoginRequestSchema)->LoginResponceSchema:
        response=self.login_api(request)
        # return LoginResponceSchema(**response.json())
        return LoginResponceSchema.model_validate_json(response.text)



def get_authentication_client()-> AuthenticationClient:
    """The function creates an instance of AuthenticationClient with the HTTP client already configured.
        :return: A ready-to-use AuthenticationClient."""
    # return AuthenticationClient(client=Client(timeout=100,base_url="http://localhost:8000")) #analog
    return AuthenticationClient(client=get_public_http_client())

#
# test_client=get_authentication_client()
# test_client.

# #without def login
# client=get_authentication_client()
# responce=client.login()
# responce_data=responce.json()
# #with def login
# client=get_authentication_client()
# responce=client.login()