from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from rest_framework import status


class Users(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse(data={})

    def post(self, request, *args, **kwargs):
        return JsonResponse(data={})


class SingleUser(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse(data={})

    def post(self, request, *args, **kwargs):
        return JsonResponse(data={})
