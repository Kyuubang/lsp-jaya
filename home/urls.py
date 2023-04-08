from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('distributor/', views.distributor, name='distributor'),
    path('purchasing/', views.purchasing, name='purchasing'),
    path('sell/', views.sell, name='sell'),
    path('medicine/', views.medicine, name='medicine'),
]
