from django.db import models

# Create your models here.

class Chat(models.Model):
    room_name = models.CharField(max_length=255)
    allowed_users = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.room_name