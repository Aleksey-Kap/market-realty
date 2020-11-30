from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('country/<int:id>/delete', views.country_delete, name='country.delete'),
    path('country/create', views.country_create, name='country.create'),
    path('country/<int:id>/add_region', views.add_region, name='country.add_region'),
    path('country/<int:id>/create_region', views.create_region, name='country.create_region'),
    ]