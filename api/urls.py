from django.urls import path

from api import views

urlpatterns = [
    path('yeet/', views.YeetView.as_view()),
]
