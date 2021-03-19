from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.files import ImageField

# Create your models here.


class UploadFile(models.Model):
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return str(self.file.name).split('/')[1]


class FileInfo(models.Model):
    file = models.OneToOneField(UploadFile, on_delete=CASCADE)
    avg_rgb = CharField(max_length=100)
    avg_image = ImageField()
    height = IntegerField()
    width = IntegerField()

    def __str__(self):
        return str(self.file)
