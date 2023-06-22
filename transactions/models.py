from django.db import models

# Create your models here.
class Transactions(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    type_currency_purchased = models.CharField(max_length=20)
    type_currency_used = models.CharField(max_length=20)
    type_of_transaction = models.CharField(max_length=10)
    amount = models.FloatField()
    purchase_price = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
