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


class UserStock(models.Model):
    customer_obj = models.ForeignKey(Customer, null=True,
                                     on_delete=models.SET_NULL)
    stock_full_name = models.CharField(max_length=128, null=True)
    stock_name = models.CharField(max_length=128, null=True)
    threshold_low = models.FloatField(verbose_name="Lower threshold alert",
                                      null=True, blank=True)
    threshold_high = models.FloatField(verbose_name="Upper threshold alert",
                                       null=True, blank=True)
    send_update = models.BooleanField(verbose_name="send update")
    last_update_sent = models.IntegerField(verbose_name="last_update_sent",
                                           null=True, blank=True, default=0)
    last_update_sent_high = models.IntegerField(verbose_name="last_update_sent_high",
                                                null=True, blank=True, default=0)
