from django.db import models
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
# Create your models here.

class PlaceInfo(models.Model):
    """Model definition for MODELNAME."""

    info_about_place = models.TextField(max_length=500)
    place_name = models.TextField(max_length=10,primary_key=True)

    def __str__(self):
        return str(self.place_name + " :   " + self.info_about_place)



class Image(models.Model):
    id= models.AutoField(primary_key=True)
    place = models.ForeignKey(PlaceInfo, on_delete=models.CASCADE)
    img = models.ImageField(upload_to ="uploads/")


    def __str__(self):
        return str(self.img)

