from django.db import models
from django.utils import timezone

class Lion(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    create_data=models.DateField(default=timezone.now)


    def __str__(self):
        return str(self.name)

