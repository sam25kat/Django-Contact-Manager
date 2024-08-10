from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_contact, name='add_contact'),
    path('', views.contact_list, name='contact_list'),
    path('search/', views.search_contact, name='search_contact'),
    path('update/<int:pk>/', views.update_contact, name='update_contact'),
    path('delete/<int:pk>/', views.delete_contact, name='delete_contact'),
]
