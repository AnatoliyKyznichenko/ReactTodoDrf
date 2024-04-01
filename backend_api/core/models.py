from django.db import models


class ToDo(models.Model):
    name = models.CharField(max_length=300)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name