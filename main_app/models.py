from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Planet(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    mass = models.IntegerField()
    distance = models.IntegerField()
    parent_star = models.CharField(max_length=100)
    dist_from_star = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
# make a migration in the terminal
    def __str__(self):
        return self.name
