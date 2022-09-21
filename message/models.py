from django.db import models
from username.models import Username

class Messages(models.Model):
    username = models.ForeignKey(Username, on_delete=models.CASCADE, related_name='messages')
    message = models.TextField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message