from django.urls import path
from . import views

urlpatterns =\
    [
        # to many paths so little time
        path('',views.index,name='index'),
        path('newbook',views.newBook,name = 'newBook'),
        path('bookview',views.bookView, name = 'bookView'),
        path('newcar',views.newCar, name = 'newCar'),
        path('allcar', views.allCar, name = 'carView'),
    ]