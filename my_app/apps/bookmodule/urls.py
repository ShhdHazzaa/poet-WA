from django.urls import path
from .views import PoemListView, PoemDetailView, PoetListView, PoetDetailView

urlpatterns = [
    path('poems/', PoemListView.as_view(), name='poem_list'),
    path('poems/<int:pk>/', PoemDetailView.as_view(), name='poem_detail'),
    path('poets/', PoetListView.as_view(), name='poet_list'),
    path('poets/<int:pk>/', PoetDetailView.as_view(), name='poet_detail'),
]
