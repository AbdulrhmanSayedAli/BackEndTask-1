from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from rest_framework import status
import json
import uuid

DATA_BASE_DIR = "courses/db.json"


def getCourses():
    database = open(DATA_BASE_DIR)
    return json.load(database)["courses"]


def generateID():
    return uuid.uuid1()


class Courses(View):
    def get(self, request, *args, **kwargs):
        courses = getCourses()
        return JsonResponse(data=courses)

    def post(self, request, *args, **kwargs):
        return JsonResponse(data={"hi(post)": "hello(post)"})


class SingleCourse(View):
    def get(self, request, *args, **kwargs):
        courses = getCourses()
        id = kwargs["id"]
        if id in courses:
            return JsonResponse(data=courses[id])

        return JsonResponse(data={"result": "404 not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        return JsonResponse(data={"hi(put)": "hello(put)"})

    def delete(self, request, *args, **kwargs):
        return JsonResponse(data={"hi(delete)": "hello(delete)"})
