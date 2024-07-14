from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit_expense/', views.submit_expense, name='submit_expense'),
    path('submit_income/', views.submit_income, name='submit_income'),
    path('delete_expense/<int:id>/', views.delete_expense, name='delete_expense'),
    path('delete_income/<int:id>/', views.delete_income, name='delete_income'),
]
