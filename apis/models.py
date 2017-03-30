from django.db import models

# Create your models here.

class Api(models.Model):
    api_name = models.CharField(max_length=200)
    api_url = models.CharField(max_length=200)
    api_parms = models.CharField(max_length=200)
    api_method = models.CharField(max_length=200)
    api_add_date = models.DateTimeField('date api added')

    def __str__(self):
        return self.api_name
