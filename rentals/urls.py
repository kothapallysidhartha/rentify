from django.urls import path
from rentals import views

urlpatterns = [
    path('',views.index,name='index'),
    path('user_login/',views.user_login,name='user_login'),
    path('register/', views.register, name='register'),
    path('property/', views.property, name='property'),
    path('property/<int:property_id>/', views.property_details, name='property_details'),
]

