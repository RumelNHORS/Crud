from django.urls import path
from myapp import views


urlpatterns = [
    path('', views.add_show, name='add_show'),
    
]
