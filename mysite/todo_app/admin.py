from django.contrib import admin
from .models import Task # Tuodaan Task-malli tästä samasta kansiosta

admin.site.register(Task)
