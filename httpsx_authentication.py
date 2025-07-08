import httpx

login_payload={
  "email": "user@example.com",
  "password": "string"
}
login_response=httpx.post("http://localhost:8000/api/v1/authentication/login",json=login_payload)
login_json_data=login_response.json()
print(f"Login response: {login_json_data}")
print(f"status code: {login_response.status_code}")

refresh_payload={
  "refreshToken": login_json_data['token']['refreshToken']
}
refresh_response=httpx.post("http://localhost:8000/api/v1/authentication/refresh",json=refresh_payload)
login_refresh_data=refresh_response.json()
print(f"Refresh response: {login_refresh_data}")
print(f"status code: {refresh_response.status_code}")