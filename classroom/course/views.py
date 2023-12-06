from django.shortcuts import render
from .models import Course

# Create your views here.
def index(req):
    courses = Course.objects.all()
    return render(req, 'course/index.html' ,{'courses': courses})