import httpx

from tools.fakers import get_random_email

# create new user
create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print('Create user data:', create_user_response_data)

# authentication for created user
login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print('Login data:', login_response_data)

# Authorization
create_file_header = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
create_file_response = httpx.post("http://localhost:8000/api/v1/files",
                                  data={"filename": "marioTest.png",
                                        "directory": "courses"},
                                  files={"upload_file": open('./testdata/files/marioTest.png', 'rb')},
                                  headers=create_file_header)
create_file_response_data=create_file_response.json()
print('Create file data:',create_file_response_data)
