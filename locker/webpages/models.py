from django.db import models

# Create your models here.


class SignUpModel(models.Model):
    first_name = models.CharField(max_length=16, blank=False)
    last_name = models.CharField(max_length=16, blank=False)
    username = models.CharField(max_length=250, blank=False, unique=True)
    email_address = models.EmailField(max_length=256, blank=False, unique=True)
    phone_number = models.CharField(max_length=14, blank=False)
    date_of_birth = models.DateField(blank=False)
