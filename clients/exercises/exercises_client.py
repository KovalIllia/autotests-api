from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class Exercise(TypedDict):
    """Description of course structure"""
    id: str
    title: str
    courseId: int
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class CreateExerciseResponseDict(TypedDict):
    """Description of the structure of the Exercise creation response"""
    exercise: Exercise


class GetExercisesResponseDict(TypedDict):
    exercises: list[Exercise]


class GetExercisesQueryDict(TypedDict):
    """Description of the structure of the request for obtaining a list of exercises."""
    courseId: str


class CreateExercisesRequestDict(TypedDict):
    """Description of the structure of the request for creating a list of exercises."""
    title: str
    course_id: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExercisesRequestDict(TypedDict):
    """Description of the structure of the request for updating a list of exercises."""
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    """Client for working with /api/v1/exercises"""

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """Method for getting a list of exercises.
        :param query: Dictionary with userId.
        :return: Response from the server as httpx.Response object"""
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """Method for getting a list of exercises.
        :param exercise_id: exercises ID.
        :return: Response from the server as httpx.Response object"""
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExercisesRequestDict) -> Response:
        """Method for creating a list of exercises.
        :param request: Dictionary with title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Response from the server as httpx.Response object"""
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExercisesRequestDict) -> Response:
        """Method for updating a list of exercises.
        :param exercise_id: Course ID.
        :param request: Dictionary with title, maxScore, minScore, description, estimatedTime.
        :return: Response from the server as httpx.Response object."""
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """Method for deleting a list of exercises.
        :param exercise_id: Course ID.
        :return: Response from the server as httpx.Response object"""
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    # def create_course(self, request: CreateExercisesRequestDict) -> CreateExerciseResponseDict:
    #     response = self.create_course_api(request)
    #     return response.json()





    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        response = self.get_exercises_api(query)
        return response.json()

    def get_exercise(self,exercise_id: str) -> Exercise:
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise(self,query: CreateExercisesRequestDict) -> CreateExerciseResponseDict:
        response = self.create_exercise_api(query)
        return response.json()


    def update_exercise(self,exercise_id: str,query: UpdateExercisesRequestDict) -> Exercise:
        response = self.update_exercise_api(exercise_id,query)
        return response.json()

def get_exercise_client(user: AuthenticationUserDict) -> ExercisesClient:
    """The function creates a FilesClient instance with the HTTP client already configured.
    :return: The FilesClient is ready to use."""
    return ExercisesClient(client=get_private_http_client(user))
