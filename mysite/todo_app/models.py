from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200) # Tehtävän nimi
    completed = models.BooleanField(default=False) # Onko tehty vai ei
    created_at = models.DateTimeField(auto_now_add=True) # Tallentaa ajan automaattisesti

    def __str__(self):
        return self.title # Näyttää tehtävän nimen hallintapaneelissa
