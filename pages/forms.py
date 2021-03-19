from django import forms
from .models import UploadFile, FileInfo


class UploadFileForm(forms.ModelForm):

    class Meta:
        model = UploadFile
        fields = ('file',)


class FileInfoForm(forms.ModelForm):

    class Meta:
        model = FileInfo
        fields = ('file', 'avg_rgb', 'avg_image', 'height', 'width')
