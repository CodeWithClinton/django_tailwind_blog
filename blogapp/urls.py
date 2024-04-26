from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("blogs/<int:pk>", views.detail, name="detail")
]
