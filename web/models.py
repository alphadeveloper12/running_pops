from django.db import models

# Create your models here.

from django.db import models

class Benefit(models.Model):
    wallet_address = models.CharField(max_length=1000)  # Assuming a maximum length for a wallet address.
    twitter_handle = models.CharField(max_length=1000, blank=True)  # Allowing the Twitter handle to be empty.
    nft_link_url = models.URLField()
    collection_name = models.CharField(max_length=1000)
    nft_number = models.CharField(max_length=1000)
    message = models.TextField(blank=True)  # Allowing the message to be empty.

    def __str__(self):
        return f"{self.wallet_address} - {self.collection_name}"


class Wallet(models.Model):
    wallet_address = models.CharField(max_length=1000)

    def __str__(self):
        return self.wallet_address
