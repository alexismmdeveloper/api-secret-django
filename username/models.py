from django.db import models

class UsernameModel(models.CharField):
    def __init__(self, *args, **kwargs):
        super(UsernameModel,self).__init__(*args, **kwargs)
    
    def get_prep_value(self, value):
        return str(value).lower()

class Username(models.Model):
    username = UsernameModel('Username', max_length=15, unique=True)

    def __str__(self):
        return self.username