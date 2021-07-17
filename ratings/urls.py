from django.urls import path
from . import views

app_name = 'ratings'

urlpatterns = [
    path('', views.home, name='home'),
    path('beers/', views.show_beers, name='show_beers'),
    path('beers/new/', views.create_beer, name='create_beer'),
    path('beers/<int:beer_id>/delete/', views.delete_beer, name='delete_beer'),
    path('beers/<int:beer_id>/', views.show_beer, name='show_beer'),
    path('beers/<int:beer_id>/edit/', views.edit_beer, name='edit_beer'),
    path('beers/<int:beer_id>/reviews/',
         views.show_reviews, name='show_reviews'),
    path('beers/<int:beer_id>/reviews/new/',
         views.create_review, name='create_review'),
    path('beers/<int:beer_id>/reviews/<int:review_id>/',
         views.show_review, name='show_review'),
    path('beers/<int:beer_id>/reviews/<int:review_id>/edit/',
         views.edit_review, name='edit_review'),
    path('beers/<int:beer_id>/reviews/<int:review_id>/delete/',
         views.delete_review, name='delete_review'),
]
