import httpx
from grpc.beta.implementations import access_token_call_credentials

#
# login_payload = {
#     "email": "user@example.com",
#     "password": "string"
# }
# login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
# login_json_data = login_response.json()
# print(f"Login response: {login_json_data}")
# print(f"status code: {login_response.status_code}")
#
# refresh_payload = {
#     "refreshToken": login_json_data['token']['refreshToken']
# }
# refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload)
# login_refresh_data = refresh_response.json()
# print(f"Refresh response: {login_refresh_data}")
# print(f"status code: {refresh_response.status_code}")
# print("---------------------------------------")

# example 2 from homework
login_payload_2 = {"email": "user1@example.com",
                   "password": "string"}
login_response_2=httpx.post("http://localhost:8000/api/v1/authentication/login",json=login_payload_2)
login_json_data_2=login_response_2.json()
# print(login_json_data_2)
access_token=login_json_data_2['token']['accessToken']
# print(access_token)
required_header = {"Authorization": f"Bearer {access_token}"}
response_from_get = httpx.get("http://localhost:8000/api/v1/users/me", headers=required_header)
# print(response_from_get.request.headers)
print(response_from_get.status_code)
print(response_from_get.json())