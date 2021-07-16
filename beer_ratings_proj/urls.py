from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("beer/", include("beer_ratings_app.urls"))
]
