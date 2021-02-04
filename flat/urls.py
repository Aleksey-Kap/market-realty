from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'flat'
urlpatterns = [
    path('', views.index, name='index'),
    path('snyat-kvartiru/', views.snyat_kvartiru, name='snyat_kvartiru'),
    path('search/', views.search, name='search'),
    path('<int:id>/', views.card, name='card'),
    ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)