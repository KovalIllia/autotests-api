import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")

print(response.status_code)  # 200
# print(response.json())       # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}


#example №2
data = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
}

response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)

# print(response.status_code)  # 201 (Created)
# print(response.json())       # response with created value
# print(response.request.headers)



#example №3
data = {"username": "test_user", "password": "123456"}

response = httpx.post("https://httpbin.org/post", data=data)

# print(response.json())  # {'form': {'username': 'test_user', 'password': '123456'}, ...}
# print(response.request.headers)



#example №4
headers = {"Authorization": "Bearer my_secret_token"}

response = httpx.get("https://httpbin.org/get", headers=headers)

# print(response.request.headers)
# print(response.json())  # Headers included in response


#example №5
params = {"userId": 1}

response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)

# print(response.url)    # https://jsonplaceholder.typicode.com/todos?userId=1
# print(response.json()) # Filtered task list

#example №6
files = {"file": ("example.txt", open("example.txt", "rb"))}

response = httpx.post("https://httpbin.org/post", files=files)

# print(response.json())  # Response with data about the uploaded file


#example №7
with httpx.Client() as client:
    response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")

# print(response1.json())  # Data of the first task
# print(response2.json())  # Data of the second task


#example №8
# client = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})
#
# response = client.get("https://httpbin.org/get")

# print(response.json())  # Headers included in response
# client.close()


#example №9
# try:
#     response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
#     response.raise_for_status()  # Will throw an exception on 4xx/5xx
# except httpx.HTTPStatusError as e:
#     print(f"Request error: {e}")



#example №10
try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout:
    print("The request has exceeded the time limit!!")
