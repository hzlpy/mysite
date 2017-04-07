from django.db import models

# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    add_project_date = models.DateTimeField('date project added', null=True)

    def __str__(self):
        return self.project_name

class Api(models.Model):
    project = models.ForeignKey(Project)
    api_name = models.CharField(max_length=200)
    api_url = models.CharField(max_length=200)
    api_parms = models.CharField(max_length=200, null=True, blank=True)
    api_method = models.CharField(max_length=200)
    api_add_date = models.DateTimeField('date api added', null=True, blank=True)

    def __str__(self):
        return self.api_name
