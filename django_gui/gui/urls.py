from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('drivers/', views.GetDriversView.as_view(), name='drivers'), 
]
