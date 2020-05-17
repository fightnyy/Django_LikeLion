from django.db import models
from django.utils import timezone
from myapp.models import Lion

# Create your models here.
class Post(models.Model):
    name = models.ForeignKey (Lion, on_delete=models.CASCADE)   # 같이 삭제하라고 알려주는 것 1:N일때 1에 해당하는(Lion)을 앞에 써줌
    title = models.CharField(max_length = 100)
    content = models.TextField(max_length = 200)
    create_data = models.DateTimeField(default = timezone.now)
    objects = models.Manager()
    
    def __str__(self):
        return str(self.title)