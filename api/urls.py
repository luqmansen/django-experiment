from django.urls import path

from api import views

urlpatterns = [
    path('yeet/', views.Yeet.as_view()),
]
