from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from rest_framework import status
import json
import uuid

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


class Courses(View):
    def get(self, request, *args, **kwargs):
        courses = getCourses()
        return JsonResponse(data=courses)

    def post(self, request, *args, **kwargs):
        courses = getCourses()
        databaseWrite = open(DATA_BASE_DIR, "w")
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        newCourse = getCourse(body)
        courses[newCourse["id"]] = newCourse
        json.dump({"courses": courses}, databaseWrite)
        databaseWrite.close()
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

        databaseWrite = open(DATA_BASE_DIR, "w")
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        updatedCourse = getCourse(body)
        updatedCourse["id"] = id
        courses[id] = updatedCourse
        json.dump({"courses": courses}, databaseWrite)
        databaseWrite.close()
        return JsonResponse(data={"result": "updated"})

    def delete(self, request, *args, **kwargs):
        id = kwargs["id"]
        courses = getCourses()
        if id not in courses:
            return JsonResponse(data={"result": "404 not found"}, status=status.HTTP_404_NOT_FOUND)
        courses.pop(id)
        databaseWrite = open(DATA_BASE_DIR, "w")
        json.dump({"courses": courses}, databaseWrite)
        databaseWrite.close()
        return JsonResponse(data={"result": "deleted"}, status=status.HTTP_200_OK)
