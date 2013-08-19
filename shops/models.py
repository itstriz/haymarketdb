from django.db import models

class ShopContact(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    phone_num = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=75, blank=True)

    def __unicode__(self):
        return self.first_name + " " + self.last_name

class ShopAddress(models.Model):
    add_date = models.DateTimeField(auto_now_add=True, editable=False)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=75)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)

class Shop(models.Model):
    name = models.CharField(max_length=255)
    add_date = models.DateTimeField(auto_now_add=True, editable=False)
    contact = models.ForeignKey(ShopContact)
    address = models.ForeignKey(ShopAddress)

    def __unicode__(self):
        return self.name
