from django.urls import path
from myapp import views


urlpatterns = [
    path('', views.add_show, name='add_show'),
    path('delete/<int:id>/', views.delete_data, name='delete-data'),
    path('update/<int:id>/', views.update_data, name='update-data'),
    
]
