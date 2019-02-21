from django.db import models
from django.utils import timezone
# Create your models here.


# for both models u added str for troubleshooting in case of issues not easily seen otherwise simple letters and numbers
# save publish date
class Book(models.Model):
    name = models.CharField(max_length=100)
    pageNumber = models.IntegerField(default=0)
    genre = models.CharField(max_length=100)
    publishDate = models.DateField(default=timezone.now())
    def __str__(self):
        return self.name

class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    def __str__(self):
        return self.make + ' ' + self.model
