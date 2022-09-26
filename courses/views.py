from wsgiref import validate
from django.views import View
from django.http import JsonResponse
from rest_framework import status
import json

from courses.models import Course
from .forms import *


def courseToJson(course):
    return json.loads(
        json.dumps({
            "id": course.id,
            "title": course.title,
            "subTitle": course.subTitle,
            "description": course.description,
            "image": course.image,
            "price": course.price,
        }
        ))


class Courses(View):
    def get(self, request, *args, **kwargs):
        courses = list(Course.objects.values())
        return JsonResponse(data=courses, safe=False)

    def post(self, request, *args, **kwargs):
        body = json.loads(request.body)
        form = CourseForm(body)
        if not form.is_valid():
            return JsonResponse(data=json.loads(form.errors.as_json()), status=status.HTTP_205_RESET_CONTENT)

        Course.objects.create(**body)
        return JsonResponse(data={"result": "created"}, status=status.HTTP_201_CREATED)


class SingleCourse(View):
    def get(self, request, *args, **kwargs):
        id = kwargs["id"]
        try:
            course = Course.objects.get(id=id)
        except Course.DoesNotExist:
            return JsonResponse(data={"result": "404 not found"}, status=status.HTTP_404_NOT_FOUND)

        return JsonResponse(data={**courseToJson(course)}, safe=False, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        id = kwargs["id"]
        try:
            course = Course.objects.get(id=id)
        except Course.DoesNotExist:
            return JsonResponse(data={"result": "404 not found"}, status=status.HTTP_404_NOT_FOUND)

        body = json.loads(request.body)
        form = CourseForm(body)
        form.unRequireAll()
        if not form.is_valid():
            return JsonResponse(data=json.loads(form.errors.as_json()), status=status.HTTP_205_RESET_CONTENT)

        for key in body:
            setattr(course, key, body[key])
        course.save()
        return JsonResponse(data={"result": "updated"})

    def delete(self, request, *args, **kwargs):
        id = kwargs["id"]
        try:
            course = Course.objects.get(id=id)
        except Course.DoesNotExist:
            return JsonResponse(data={"result": "404 not found"}, status=status.HTTP_404_NOT_FOUND)

        course.delete()
        return JsonResponse(data={"result": "deleted"}, status=status.HTTP_200_OK)
