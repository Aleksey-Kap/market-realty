from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('country/<int:id>/delete', views.country_delete, name='country.delete'),
    path('country/create', views.country_create, name='country.create'),
    path('country/<int:id>/add_region', views.add_region, name='country.add_region'),
    path('country/<int:id>/create_region', views.create_region, name='country.create_region'),
    path('region/<int:id>/delete', views.region_delete, name='region.delete'),
    path('region/<int:id>/add_child', views.add_child_region, name='region.add_child'),
    path('region/<int:id>/create_child', views.create_child_region, name='region.create_child'),
    path('region/<int:id>/add_city', views.add_city, name='region.add_city'),
    path('region/<int:id>/create_city', views.create_city, name='region.create_city'),
    path('city/<int:id>/delete', views.city_delete, name='city.delete'),

    ]