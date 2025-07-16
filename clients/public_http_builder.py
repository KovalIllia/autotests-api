from httpx import Client

def get_public_http_client() -> Client:
    """The function creates httpx.Client instance with basic settings.
    :return: A ready-to-use httpx.Client object.
    without headers authorization"""
    return Client(timeout=100,base_url="http://localhost:8000")