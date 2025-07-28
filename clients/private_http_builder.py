from httpx import Client
from pydantic import BaseModel

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema
from typing import TypedDict

class AuthenticationUserSchema (BaseModel):
    """User data structure for authorization"""
    email: str
    password: str

def get_private_http_client(user:AuthenticationUserSchema)-> Client:
    """The function creates as httpx.Client instance with user authentication.
    :param user: AuthenticationUserSchema object with the user's email and password.
    :return: A ready-to-use httpx.Client object with the Authorization header set."""
    authentication_client=get_authentication_client()

    login_request = LoginRequestSchema(email=user.email, password=user.password)
    login_response =authentication_client.login(login_request)

    return Client(timeout=100,
                  base_url="http://localhost:8000",
                  headers={"Authorization": f"Bearer {login_response.token.access_token}"})

