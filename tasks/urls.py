from django.urls import path, include

from tasks import views


tasks_urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', include([
        path('', views.create, name='create'),
    ])),
]

tasks_api_urlpatterns = [

]