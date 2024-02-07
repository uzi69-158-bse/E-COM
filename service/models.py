from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    project = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name
    

class dynamicService(models.Model):
    service_icon = models.CharField(max_length=255)
    service_name = models.CharField(max_length=255)
    service_description = models.TextField()


