from django.urls import path, include

from tasks import views


tasks_urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', include([
        path('', views.create, name='create'),
        path('<int:task_id>/', views.detail, name='detail'),
        path('<int:task_id>/delete/', views.delete, name='delete'),
    ])),
]

tasks_api_urlpatterns = [
    path('tasks/', include([
        path('', )
    ])),
]