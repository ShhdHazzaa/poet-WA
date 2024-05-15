from django.urls import path
from .views import (PoemListView, PoemDetailView, PoemCreateView, 
                    PoemUpdateView, PoemDeleteView, PoetListView, PoetDetailView)

urlpatterns = [
    path('', PoemListView.as_view(), name='poem_list'),
    path('poem/<int:pk>/', PoemDetailView.as_view(), name='poem_detail'),
    path('poem/new/', PoemCreateView.as_view(), name='poem_create'),
    path('poem/<int:pk>/edit/', PoemUpdateView.as_view(), name='poem_edit'),
    path('poem/<int:pk>/delete/', PoemDeleteView.as_view(), name='poem_delete'),
    path('poets/', PoetListView.as_view(), name='poet_list'),
    path('poet/<int:pk>/', PoetDetailView.as_view(), name='poet_detail'),
]
