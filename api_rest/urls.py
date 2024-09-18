from django.urls import path
from . import views

urlpatterns = [

    path('',views.get_users,name='get_users_url'),
    path('user/<str:nick>',views.get_user_by_id)
    
]
