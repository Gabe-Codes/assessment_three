from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.widget_create, name='widget_create'),
    path('delete/<int:widget_id>', views.widget_delete, name='widget_delete'),
]