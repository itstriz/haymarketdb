from django.db import models

class Shop(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Member(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True, editable=False)
    shop = models.ForeignKey(Shop)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    start_date = models.DateTimeField('membership started')

    def __unicode__(self):
        return self.last_name + ", " + self.first_name
    
