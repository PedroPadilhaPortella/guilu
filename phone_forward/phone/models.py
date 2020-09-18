from django.db import models

# Create your models here.
class Func(models.Model):
    phone_number = models.CharField(max_length = 15, unique=True)
    alias = models.CharField(max_length = 60)

    @staticmethod
    def createFunc(phone_number, alias):
        if("+" not in phone_number):
            phone_number = "+" + phone_number
        return Func(phone_number = phone_number, alias = alias)