from django.contrib import admin
from .models import UploadFile, FileInfo
# Register your models here.

admin.site.register([UploadFile, FileInfo])
