from typing import Any

from httpx import Client, URL, QueryParams, Response
from httpx._types import RequestData, RequestFiles


class APIClient():
    def __init__(self, client: Client):
        """A basic API client that accepts an httpx.Client object.

        :param client: httpx.Client instance to make HTTP requests"""
        self.client = client

    def get(self, url: URL | str, params: QueryParams | None = None)-> Response:
        """Performs a GET request.
        :param url: The URL of the endpoint.
        :param params: The GET parameters of the request (e.g. ?key=value).
        :return: The Response object with the response data."""
        return self.client.get(url, params=params)


    def post(
            self,
            url: URL | str,
            json: Any | None = None,  # optional field
            data: RequestData | None = None,  # optional field
            files: RequestFiles | None = None  # optional field
    ) -> Response:
        """Performs a POST request.
        :param url: The URL of the endpoint.
        :param json: The data in JSON format.
        :param data: The formatted form data (e.g. application/x-www-form-urlencoded).
        :param files: The files to upload to the server.
        :return: A Response object with the response data."""
        return self.client.post(url, json=json, data=data, files=files)



    def patch(self, url: URL | str, json: Any | None = None) -> Response:
        """performs a PATCH request (partial data update).
        :param url: URL of the endpoint.
        :param json: Data to update in JSON format.
        :return: Response object with response data."""
        return self.client.patch(url, json=json)



    def delete(self, url: URL | str) -> Response:
        """Performs a DELETE request (delete data).
        :param url: URL of the endpoint.
        :return: Response object with response data."""
        return self.client.delete(url)
