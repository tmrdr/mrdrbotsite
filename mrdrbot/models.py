from django.db import models

# Create your models here.
class TextFood(models.Model):
    food = models.TextField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.food
        return self.name

class Toggled(models.Model):
    onstatus = models.BooleanField(default = False)

    def __bool__(self):
        return self.onstatus
