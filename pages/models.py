from django.db import models

# Create your models here.


class UploadFile(models.Model):
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return str(self.pk)
