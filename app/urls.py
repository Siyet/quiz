from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include
from app import views

urlpatterns = [
    path('', views.startPage if not settings.SHALARU_MODE else views.question1, name="home"),
    path('teams', views.teams, name="teams"),
    path('categories', views.categories, name="categories"),
    path('<int:cat_id>/question', views.question, name="question"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
