from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class GetCoursesQueryDict(TypedDict):
    """Description of the structure of the request for obtaining a list of courses."""
    userId: str


class CreateCoursesRequestDict(TypedDict):
    """Description of the structure of the request for creating a course."""
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str

class UpdateCoursesRequestDict(TypedDict):
    """Description of the structure of the request for updating a course."""
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None


class CoursesClient(APIClient):
    """Client for working with /api/v1/courses"""

    def get_course_api(self, query: GetCoursesQueryDict) -> Response:
        """Method for getting a list of courses.
        :param query: Dictionary with userId.
        :return: Response from the server as httpx.Response object"""
        return self.get("/api/v1/courses", params=query)


    def get_course_api(self, course_id: str) -> Response:
        """Method for getting a course.
        :param course_id: Course ID.
        :return: Response from the server as httpx.Response object"""
        return self.get(f"/api/v1/courses/{course_id}")


    def create_course_api(self, request: CreateCoursesRequestDict) -> Response:
        """Method for creating a course.
        :param request: Dictionary with title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Response from the server as httpx.Response object"""
        return self.post("/api/v1/courses", json=request)


    def update_course_api(self, course_id: str, request:UpdateCoursesRequestDict)-> Response:
        """Method for updating a course.
        :param course_id: Course ID.
        :param request: Dictionary with title, maxScore, minScore, description, estimatedTime.
        :return: Response from the server as httpx.Response object."""
        return self.patch(f"/api/v1/courses/{course_id}",json=request)


    def delete_course_api(self,course_id: str)->Response:
        """Method for deleting a course.
        :param course_id: Course ID.
        :return: Response from the server as an httpx.Response object"""
        return self.delete(f"/api/v1/courses/{course_id}")