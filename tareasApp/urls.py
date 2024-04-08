from django.urls import path
from . import views

app_name = 'tareasApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('nuevaTarea/', views.nuevaTarea, name='nuevaTarea')
]