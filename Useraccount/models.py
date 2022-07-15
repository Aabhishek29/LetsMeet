from django.db import models


class Accounts(models.Model):
    profile_image = models.ImageField(blank=True)

    name = models.CharField(max_length=50, null=False, blank=False)

    phone_number = models.IntegerField(blank=False, null=False)

    email = models.EmailField(max_length=100, null=False, blank=False, unique=True)

    password = models.CharField(max_length=20, null=False, blank=False)
    
    confirm_password = models.CharField(max_length=20, null=False, blank=False)

    # unique Id created by backend for identify person-to-person uniquely
    userId = models.CharField(max_length=20, primary_key=True, null=False, blank=False)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.userId
