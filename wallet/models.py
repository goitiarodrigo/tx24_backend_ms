from django.db import models

# Create your models here.
class Wallet(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    crypto_name = models.CharField(max_length=20)
    balance = models.FloatField()