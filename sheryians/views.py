from django.shortcuts import render
from .models import Frontend


# Create your views here.
def home(request):
    front = Frontend(
        des="Frontend Development",
        language="HTML, CSS, JavaScript",
        discount="60%",
        price=4999
    )
    return render(request, 'home.html',{'front': front})
def course(request):
    return render(request, 'courses.html')
def video2(request):
    return render(request,"video2.html")
def video3(request):
    return render(request,"video3.html")
def video4(request):
    return render(request,"video4.html")
def video5(request):
    return render(request,"video5.html")
def bootcamp(request):
    return render(request,"bootcamp.html")