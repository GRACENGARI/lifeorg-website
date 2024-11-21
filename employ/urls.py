from django.urls import path
from.import views


app_name ='employ'


urlpatterns = [
    path('',views.index,name='index'),
    path('service/', views.service, name='service'),
    path('portfolio/', views.service, name='portfolio'),
    path('starter/', views.portfolio, name='starter'),
    
]

