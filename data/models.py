from django.db import models
from username.models import Username

class Data(models.Model):
    username = models.ForeignKey(Username, on_delete=models.CASCADE, related_name='user')
    created = models.DateTimeField(auto_now_add=True)
