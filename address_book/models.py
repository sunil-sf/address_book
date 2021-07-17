from django.db import models


class AddressBook(models.Model):
    name = models.CharField(max_length=120)
    street_address = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    zip_code = models.CharField(max_length=12)

    def __str__(self):
        return self.name