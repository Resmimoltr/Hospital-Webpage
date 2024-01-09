from django.http import HttpResponse
from django.shortcuts import render
from .models import Departments
from .models import Doctor
# Create your views here.


def home(request):
    person = {
        'name': 'Resmi',
        'age': '29',
        'place': 'Cochin'
    }
    return render(request, "home.html", person)
def contact(request):
    return render(request, "contact.html")


def department(request):
    # numbers = {'list1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request, "department.html",dict_dept )


def doctors(request):

    dict_doc={
        'doc':Doctor.objects.all()
    }
    return render(request, "doctors.html",dict_doc )
    


def booking(request):
    return render(request, "booking.html")
def about(request):
    data = {
        'number': -25
    }
    return render(request, "about.html", data)
