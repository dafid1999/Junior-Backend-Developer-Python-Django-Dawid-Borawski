from django.urls import path
from . import views

app_name = 'text_processor'

urlpatterns = [
    path('', views.upload_file, name='upload'),
    path('result/', views.show_result, name='result'),
]
