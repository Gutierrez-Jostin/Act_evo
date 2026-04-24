from django.contrib import admin
from django.urls import path
from .views import home, detail_book

urlpatterns = [
    path('', home, name='home'),
    path('book/<int:id>/', detail_book, name='detail_book'),
]