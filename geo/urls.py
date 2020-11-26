from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('country/<int:id>/delete', views.country_delete, name='country.delete')
    ]