from django.urls import path
from . import views


urlpatterns = [
    path('api/jokes', views.JokeList.as_view(), name='joke_list'),
    path('api/jokes/<int:pk>', views.JokeDetail.as_view(), name='joke_detail'),
]