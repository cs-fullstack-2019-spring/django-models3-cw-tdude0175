from django.contrib import admin
from .models import Book
from .models import Car
# Register your models here.

# give admin power
admin.site.register(Book)
admin.site.register(Car)