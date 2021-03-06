from django.db import models
from django.utils.timezone import now

class Blog(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    dateStamp =  models.DateTimeField(default=now)

    def __str__(self):
        return self.title
