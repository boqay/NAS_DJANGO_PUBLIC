from django.shortcuts import render
from django.http import HttpResponse
from polls.models import User
from argon2 import PasswordHasher
import argon2
# Create your views here.

def index(request):
    if request.method == "GET":

        user_exists = User.objects.filter(id=request.GET["userId"]).exists()
        if not user_exists:
            msg = "아이디가 존재하지 않습니다."
        else:
            user = User.objects.get(id=request.GET["userId"])
            try:
                pwd_chk = PasswordHasher().verify(user.pwd, request.GET["password"])
            except argon2.exceptions.VerifyMismatchError:
                msg = "비밀번호가 일치하지 않습니다."
            else:
                msg = "로그인 되었습니다."


        rs = HttpResponse(msg)
    else:
        rs = HttpResponse("Hello, world. You're request method is POST")
    return rs
