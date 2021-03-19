from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.files import ImageField

# Create your models here.


class UploadFile(models.Model):
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return str(self.file.name).split('/')[1]

    class Meta:
        verbose_name = 'File'


class FileInfo(models.Model):
    file = models.OneToOneField(UploadFile, on_delete=models.CASCADE)
    avg_rgb = CharField(max_length=100)
    avg_image = ImageField()
    height = IntegerField(default=0)
    width = IntegerField(default=0)
    num_of_coins = IntegerField(default=0)
    sum_of_coins = IntegerField(default=0)

    def __str__(self):
        return str(self.file)

    class Meta:
        verbose_name = 'Result'
