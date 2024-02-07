from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

class News(models.Model):
    News_title = models.CharField(max_length=200)
    News_description = HTMLField()
    News_slug = AutoSlugField(populate_from= "News_title",unique=True,null= True,default=None)


# Create your models here.
