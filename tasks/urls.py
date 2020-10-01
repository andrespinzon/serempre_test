from django.urls import path

from tasks import views


tasks_urlpatterns = [
    path('', views.index, name='index'),
]

tasks_api_urlpatterns = [

]