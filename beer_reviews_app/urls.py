from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.beer_list, name="beers_list"),
    path('new', views.new_beer, name='new_beer'),
    path('<int:beer_id>', views.beer_detail, name='beer_detail'),
    path('<int:beer_id>/edit', views.edit_beer, name='edit_beer'),
    path('<int:beer_id>/delete', views.delete_beer, name='delete_beer'),
    path('<int:beer_id>/reviews', views.review_list, name='review_list'),
    path('<int:beer_id>/reviews/new', views.new_review, name='new_review'),
    path('<int:beer_id>/reviews/<int:review_id>', views.review_detail, name='review_detail'),
    path('<int:beer_id>/reviews/<int:review_id>/edit', views.edit_review, name='edit_review'),
    
]
