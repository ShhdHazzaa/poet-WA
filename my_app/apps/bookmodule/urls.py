from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('poem/<int:pk>/', views.poem_detail, name='poem_detail'),
    path('poet/<int:pk>/', views.poet_detail, name='poet_detail'),
    path('poet/', views.poet_list, name='poet_list'),
]
