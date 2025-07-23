from pydantic import BaseModel, Field, ConfigDict, HttpUrl,ValidationError
from pydantic.alias_generators import to_camel


class CourseSchema(BaseModel):
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str


course_nested_objects_model = CourseSchema(
    id="course-id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright",
    estimatedTime="1 week"
)
# print(f"Course default model: {course_default_model}")

# example_2
course_dict_nested_objects_model = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "estimatedTime": "1 week"
}
course_dict_model_nested_objects_model = CourseSchema(**course_dict_nested_objects_model)  # unpacking
# json_unpacking=CourseSchema(**response.json())#alyernative unpacking
# print(f"Course dict model: {course_dict}")


# example_3
course_json = {

    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "estimatedTime": "1 week"
}


# course_json_model=CourseSchema.model_validate_json(course_json)
# print(f"Course json model: {course_json_model}")


# example_4 Alias
class CourseSchema_4(BaseModel):
    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


alias_course_model = CourseSchema_4(
    id="course-id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright",
    estimatedTime="1 week"
)


# print(f"Alias course shema: {alias_course_model}")
#
# print(alias_course_model.model_dump())#revert of serialization without alias: json-->dict
#
# print(alias_course_model.model_dump_json())#revert of serialization without alias: json-->json.string
#
# print(alias_course_model.model_dump(by_alias=True))#revert of serialization with alias: json-->dict
# print(alias_course_model.model_dump_json(by_alias=True))#revert of serialization with alias: json-->json.string


# example_5
# alias_generator
class Course_Shema_4(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    id: str
    title: str
    max_score: int
    min_score: int
    # max_score: int = Field(alias="maxScore")
    # min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str
    # estimated_time: str = Field(alias="estimatedTime")


course_data_alias_generator = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "estimatedTime": "1 week"
}


# course_model_alias_generator=Course_Shema_4(**course_data_alias_generator)
# print(course_model_alias_generator.model_dump(by_alias=True))


# example_6 default_values

class Course_Shema_6(BaseModel):
    id: str = "course-id"
    title: str = "Playwright"
    max_score: int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=100)
    description: str = "Playwright course"
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")


# course_data_default_values=Course_Shema_6()
# print(f"data_default_values : {course_data_default_values}")


# example_7 default_factory
import uuid


class Course_Schema_7(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    max_score: int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=100)
    description: str = "Playwright course"
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")


# course_data_default_factory_values_1=Course_Schema_7()
# course_data_default_factory_values_2=Course_Schema_7()
# print(f"course_data_default_factory_values: {course_data_default_factory_values_1.id}")
# print(f"course_data_default_factory_values: {course_data_default_factory_values_2.id}")

# alternative
# class Course_Shema_8(BaseModel):
#     model_config = ConfigDict(alias_generator=to_camel,populate_by_name=True)
#     id: str=Field(default_factory=get_random_email)
#     title: str
#     max_score: int
#     min_score: int
#     # max_score: int = Field(alias="maxScore")
#     # min_score: int = Field(alias="minScore")
#     description: str
#     estimated_time: str
#     # estimated_time: str = Field(alias="estimatedTime")
#
# course_data_alias_generator_2={
#
#     "title": "Playwright",
#     "maxScore": 100,
#     "minScore": 10,
#     "description": "Playwright",
#     "estimatedTime": "1 week"
# }
# course_model_alias_generator_2=Course_Shema_8(**course_data_alias_generator_2)
# print(course_model_alias_generator_2.model_dump(by_alias=True))


# example_8 Nested structures
# Pydantic models can use nested structures, which allows us to more accurately describe complex JSON objects.

# schema for File
class FileSchema(BaseModel):
    id: str
    url: str
    filename: str
    directory: str


# schema for User
class UserSchema(BaseModel):
    id: str
    email: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CourseSchema_8(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "Playwright"
    max_score: int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=100)
    description: str = "Playwright course"
    # Nested object for preview file
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")
    # Nested object for the user who created the course
    created_by_user: UserSchema = Field(alias="createdByUser")


# Initialize the CourseSchema model by passing arguments
course_nested_objects_model = CourseSchema_8(
    id="course-id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright",
    # Added initialization of nested FileSchema model
    previewFile=FileSchema(
        id="file-id",
        url="http://localhost:8000",
        filename="file.png",
        directory="courses",
    ),
    estimatedTime="1 week",
    # Added initialization of the nested UserSchema model
    createdByUser=UserSchema(
        id="user-id",
        email="user@gmail.com",
        lastName="Bond",
        firstName="Zara",
        middleName="Alise"
    )
)
# print('Course default model:', course_nested_objects_model)

# Initialization with dict (dictionary unpacking)

# Initialize the CourseSchema model by unpacking the dictionary
course_dict_nested_objects_model = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    # Added previewFile key
    "previewFile": {
        "id": "file-id",
        "url": "http://localhost:8000",
        "filename": "file.png",
        "directory": "courses"
    },
    "estimatedTime": "1 week",
    # Added key createdByUser
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alise"
    }
}


# course_dict_model_nested_objects_model = CourseSchema(**course_dict_nested_objects_model)
# print('Course dict model:', course_dict_model_nested_objects_model)


# example_9 Methods in Pydantic models
class UserSchema_9(BaseModel):
    id: str
    email: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    def get_username(self) -> str:
        return f"{self.first_name} {self.last_name}"

    # need --> from pydantic import computed_field
    def username(self) -> str:
        return f"{self.first_name} {self.last_name}"


created_user_9 = UserSchema_9(
    id="user-id",
    email="user@gmail.com",
    lastName="Bond",
    firstName="Zara",
    middleName="Alise"
)


# print(created_user_9.get_username())
# print(created_user_9.username())


# example_10 Built-in types
# Pydantic provides a number of built-in types that help validate data automatically.
# need to import -->from pydantic import EmailStr, HttpUrl

class FileSchema_10(BaseModel):
    id: str
    url: HttpUrl  # Use HttpUrl instead of str
    file: str
    directory: str


class UserSchema_10(BaseModel):
    id: str
    email: HttpUrl  # Use HttpUrl instead of str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="fistName")
    middle_name: str = Field(alias="middleName")

    def get_username_10(self) -> str:
        return f"{self.first_name} {self.last_name}"


created_user_10 = UserSchema_10(
    id="user-id",
    email="user@gmail.com",
    lastName="Bond",
    firstName="Zara",
    middleName="Alise"
)


# print(created_user_10.get_username_10())


#work with errors
# need --> from pydantic import ValidationError
try:
    created_file_10 = FileSchema_10(
        id="file-id",
        url="http://localhost:8000",
        filename="file.png",
        directory="courses"
    )
except ValidationError as error:
    print(error)
