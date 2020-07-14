from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.


def BaseIndex(request):
    return render(request,'index.html')


def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('SuperAdminHome')

    return HttpResponse("login failed")
