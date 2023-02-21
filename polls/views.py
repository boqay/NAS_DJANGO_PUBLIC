from django.shortcuts import render
from django.http import HttpResponse
from polls.models import User
from argon2 import PasswordHasher
# Create your views here.

def index(request):
    if request.method == "GET":
        print(request.GET["userId"])
        user = User.objects.get(id=request.GET["userId"])
        print(user)
        # for Users in User.objects.all():
        #     print(Users.id)
        #     print(Users.email)
        # print(request.GET.get("userId"))

        rs = HttpResponse("User Create Success!")
    else:
        rs = HttpResponse("Hello, world. You're request method is POST")
    return rs
