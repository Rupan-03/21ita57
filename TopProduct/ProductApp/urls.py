from django.urls import path
from .views import RetriveOperationView
urlpatterns = [
    path('userInput/',RetriveOperationView.as_view(),name='UserInput'),
]