from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
from .models import Book
# Create your views here.

# for basic index and basic input added views so easier to know which one to go through
def index(request):
    return HttpResponse("newbook <br> bookview <br> newcar <br> allcar <br>")


# returning all books so easy view of what is in books
def newBook(request):
    newBook = Book(name = 'Hobbit', pageNumber = 200, genre = 'fantasy', publishDate = '1997-12-05')
    newBook.save()
    return HttpResponse(Book.objects.all())

# runs through all books with certain parameters and since new book is fixed
# this won't show anything unless added through admin
def bookView(request):
    bookArray = Book.objects.filter(publishDate__gte = '2018-01-01') #yes this work, i don't like it
    namePrint = ''
    for eachElement in bookArray:
        namePrint += eachElement.name + '<br>'
    return HttpResponse(namePrint)

# adds car, only used interger for year for readability
def newCar(request):
    newCar =Car(make = 'Dodge', model ='Charger', year = 2015)
    newCar.save()
    return HttpResponse(Car.objects.all())


# since year is only an int this works easier than {bookView} otherwise same kind of code with a bit extra
def allCar(request):
    carArray = Car.objects.filter(year__gte =2010)
    namePrint = ''
    for eachElement in carArray:
        namePrint += eachElement.make + ' ' + eachElement.model + '<br>'
    return HttpResponse(namePrint)