from django.db import models

# Create your models here.
class Event(models. Model):
    title = models. CharField(max_length=200)
    created_at = models. DateTimeField(auto_now_add=True)
    description = models. TextField()
    price = models. IntegerField()
    venue = models. CharField(max_length=200)
    date_time = models. DateTimeField()
    capcity = models. PositiveIntegerField()