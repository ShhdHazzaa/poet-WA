from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.poet_list, name='poet_list'),
    path('poet/<int:pk>/', views.poet_detail, name='poet_detail'),
    path('poem/<int:pk>/', views.poem_detail, name='poem_detail'),
]
