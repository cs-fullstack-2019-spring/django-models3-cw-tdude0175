from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
from .models import Book
# Create your views here.

def index(request):
    return HttpResponse("test")

def newBook(request):
    newBook = Book(name = 'Hobbit', pageNumber = 200, genre = 'fantasy', publishDate = '1997-12-05')
    newBook.save()
    return HttpResponse(Book.objects.all())


def bookView(request):
    bookArray = Book.objects.filter(publishDate__gte = '2018-01-01')
    namePrint = ''
    for eachElement in bookArray:
        namePrint += eachElement.name + '<br>'
    return HttpResponse(namePrint)

def newCar(request):
    newCar =Car(make = 'Dodge', model ='Charger', year = 2015)
    newCar.save()
    return HttpResponse(Car.objects.all())


def allCar(request):
    carArray = Car.objects.filter(year__gte =2010)
    namePrint = ''
    for eachElement in carArray:
        namePrint += eachElement.make + ' ' + eachElement.model + '<br>'
    return HttpResponse(namePrint)