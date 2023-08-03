from django.contrib import admin
from django.urls import path
from . import views



urlpatterns=[
    path('',views.register,name='base'),
    path('add_event/',views.add_event,name='add_event'),
    path('search', views.search, name='search'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('<int:item_id>',views.item_detail, name='item_detail'),
    path('delete/<int:id>/',views.delete,name='delete'),
    
]
