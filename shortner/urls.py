from django.urls import path

from . import views

app_name = 'shortner'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<str:pk>/', views.go, name='go')
]
