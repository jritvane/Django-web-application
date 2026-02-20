from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    # Tämä reitti nappaa tehtävän ID-numeron (esim. /delete/3/) ja vie sen poistonäkymään
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]