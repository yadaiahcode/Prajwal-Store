from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home,name="home"),
    path('product/',views.product,name="product"),
    path('add/',views.add,name="add"),
    path('list/',views.list,name="list"),
    path('details/<int:pk>/',views.details,name="detail"),
    path('edit/<int:pk>/',views.edit,name="edit"),
    path('delete/<int:pk>/',views.delete,name="delete"),
    ]