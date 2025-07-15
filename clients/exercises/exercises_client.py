from clients.api_client import APIClient
from typing import TypedDict
from httpx import Response

class GetExercisesQueryDict(TypedDict):
    """Description of the structure of the request for obtaining a list of exercises."""
    courseId:str

class CreateExercisesQueryDict(TypedDict):
    """Description of the structure of the request for creating a list of exercises."""
    title: str
    course_id:str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class UpdateExercisesQueryDict(TypedDict):
    """Description of the structure of the request for updating a list of exercises."""
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class ExercisesClient(APIClient):
    """Client for working with /api/v1/exercises"""

    def get_exercises_api(self, query:GetExercisesQueryDict)->Response:
        """Method for getting a list of exercises.
        :param query: Dictionary with userId.
        :return: Response from the server as httpx.Response object"""
        return self.get("/api/v1/exercises",params=query)

    def get_exercises_api(self, exercise_id:str)->Response:
        """Method for getting a list of exercises.
        :param exercise_id: exercises ID.
        :return: Response from the server as httpx.Response object"""
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self,request:CreateExercisesQueryDict)->Response:
        """Method for creating a list of exercises.
        :param request: Dictionary with title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Response from the server as httpx.Response object"""
        return self.post("/api/v1/exercises",json=request)

    def update_exercise_api(self, exercise_id:str, request:UpdateExercisesQueryDict)->Response:
        """Method for updating a list of exercises.
        :param exercise_id: Course ID.
        :param request: Dictionary with title, maxScore, minScore, description, estimatedTime.
        :return: Response from the server as httpx.Response object."""
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id:str)->Response:
        """Method for deleting a list of exercises.
        :param exercise_id: Course ID.
        :return: Response from the server as httpx.Response object"""
        return self.delete(f"/api/v1/exercises/{exercise_id}")