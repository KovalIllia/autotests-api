from api_client_get_user import create_user_request
from clients.courses.courses_client import get_courses_client,CreateCourseRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email

public_users_client=get_public_users_client()
create_user_request=CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)
create_user_response = public_users_client.create_user(create_user_request)

authentication_user=AuthenticationUserSchema(
    email=create_user_request['email'],
    password=create_user_request['password']
)
files_client=get_files_client(authentication_user)
courses_client=get_courses_client(authentication_user)

create_file_request = CreateFileRequestDict(
    filename="marioTest.png",
    directory="courses",
    upload_file="./testdata/files/marioTest.png"
)
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

create_course_request = CreateCourseRequestDict(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)

create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)