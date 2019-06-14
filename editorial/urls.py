from django.urls import path
from editorial import views
from django.contrib import admin


urlpatterns = [
    path('admin', admin.site.urls),
    path("", views.today_editorial, name="today_editorial"),
]