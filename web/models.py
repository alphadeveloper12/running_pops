from django.db import models

# Create your models here.



class NFTWalletForm(models.Model):
    wallet_address = models.CharField(max_length=1000)

    def __str__(self):
        return self.email
