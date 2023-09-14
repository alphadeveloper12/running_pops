from django.db import models

# Create your models here.



class Wallet(models.Model):
    wallet_address = models.CharField(max_length=1000)

    def __str__(self):
        return self.wallet_address
