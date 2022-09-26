from wsgiref import validate
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from rest_framework import status
import json
import uuid

from courses.models import Course
from .forms import *
DATA_BASE_DIR = "courses/db.json"


def getCourses():
    database = open(DATA_BASE_DIR, "r")
    result = json.load(database)["courses"]
    database.close()
    return result


def generateID():
    return str(uuid.uuid1())


def getCourse(body):
    return {
        "id": generateID(),
        "title": body["title"],
        "subTitle": body["subTitle"],
        "description": body["description"],
        "image": body["image"],
        "price": body["price"],
    }


def updateData(courses):
    databaseWrite = open(DATA_BASE_DIR, "w")
    json.dump({"courses": courses}, databaseWrite)
    databaseWrite.close()


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
        courses = getCourses()
        id = kwargs["id"]
        if id in courses:
            return JsonResponse(data=courses[id])

        return JsonResponse(data={"result": "404 not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        id = kwargs["id"]
        courses = getCourses()
        if id not in courses:
            return JsonResponse(data={"result": "404 not found"}, status=status.HTTP_404_NOT_FOUND)

        body = json.loads(request.body)

        form = CourseForm(body)
        form.unRequireAll()
        if not form.is_valid():
            return JsonResponse(data=json.loads(form.errors.as_json()), status=status.HTTP_205_RESET_CONTENT)

        updatedCourse = courses[id]
        # update only passed data
        for key in body:
            if key in updatedCourse:
                updatedCourse[key] = body[key]

        courses[id] = updatedCourse
        updateData(courses)
        return JsonResponse(data={"result": "updated"})

    def delete(self, request, *args, **kwargs):
        id = kwargs["id"]
        courses = getCourses()
        if id not in courses:
            return JsonResponse(data={"result": "404 not found"}, status=status.HTTP_404_NOT_FOUND)
        courses.pop(id)
        updateData(courses)
        return JsonResponse(data={"result": "deleted"}, status=status.HTTP_200_OK)
