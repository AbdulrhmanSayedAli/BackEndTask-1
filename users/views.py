from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from rest_framework import status
from .models import User
from .forms import UserForm
import json


def userToJson(user):
    return json.loads(
        json.dumps({
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "name": user.name,
            "email": user.email,
            "password": user.password,
            "birthDate": str(user.birthDate),
            "age": user.age
        }
        ))


def filterByAge(users, min_age):
    result = []
    for user in users:
        if user.age >= min_age:
            result.append(userToJson(user))
    return result


class Users(View):
    def get(self, request, *args, **kwargs):
        min_age = 0
        if "min_age" in request.GET:
            min_age = int(request.GET["min_age"])

        users = list(User.objects.all())
        users = filterByAge(users, min_age)
        return JsonResponse(data=users, safe=False)


class SingleUser(View):
    def get(self, request, *args, **kwargs):
        id = kwargs["id"]
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return JsonResponse(data={"result": "404 not found"}, status=status.HTTP_404_NOT_FOUND)

        return JsonResponse(data={**userToJson(user)}, safe=False, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        return JsonResponse(data={})
