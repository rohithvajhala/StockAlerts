from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True,
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=128, blank=True)
    email = models.EmailField(max_length=128, unique=True)

    def __str__(self):
        return self.name
