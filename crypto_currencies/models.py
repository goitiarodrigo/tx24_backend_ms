from django.db import models

# Create your models here.
class Crypto_Currency(models.Model):
    name = models.CharField(max_length = 20)
    image = models.URLField(max_length = 300)
    abbreviation = models.CharField(max_length = 15)
    old_price = models.FloatField()
    current_price = models.FloatField()
    previous_day_price = models.FloatField()