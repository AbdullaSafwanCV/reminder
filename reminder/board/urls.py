from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('completed/<int:id>/', views.completed, name='completed'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:pk>/', views.edit_reminder, name='edit_reminder'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
]