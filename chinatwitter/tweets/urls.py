from django.urls import path
from tweets import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('tweets/', views.tweet_list_view, name="tweet_list"),
    path('create-tweet/', views.tweet_create_view, name="tweet_create"),
    path('tweets/<int : tweet_id>', views.tweet_view, name="tweets"),
]
