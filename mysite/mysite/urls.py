from django.contrib import admin
from django.urls import path, include # Varmista, että 'include' on tässä

urlpatterns = [
    path('admin/', admin.site.urls), # Huom: Tämän kuuluu olla admin.site.urls
    path('', include('todo_app.urls')), # Tämä ohjaa etusivun sovellukseesi
]

