from pages.forms import FileInfoForm
from django.http.response import JsonResponse
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import redirect, render
import cv2
import numpy as np
import os
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import io
import time
from config import settings
from .models import FileInfo, UploadFile

# from somewhere import handle_uploaded_file


class HomePageView(TemplateView):
    template_name = 'home.html'


class ResultPageView(TemplateView):
    template_name = 'result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['files'] = FileInfo.objects.all()
        return context


def file_upload_view(request):
    # print(request.FILES)
    if request.method == 'POST':
        my_file = request.FILES.get('file')
        up_file = UploadFile.objects.create(file=my_file)
        height, width = get_file_size(up_file.file.name)
        avg_color = get_average_color(up_file.file.name)
        avg_image = create_image(avg_color)
        file_info = FileInfo(file=up_file, avg_rgb=avg_color,
                             avg_image=avg_image, height=height, width=width)
        file_info.save()
        return HttpResponse('')
    return JsonResponse({'post': 'false'})


def get_file_size(file):
    img = cv2.imread(os.path.join(settings.MEDIA_ROOT, file))
    height, width, _ = img.shape
    return height, width


def get_average_color(file):
    img = cv2.imread(os.path.join(settings.MEDIA_ROOT, file))
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    average = rgb_img.mean(axis=0).mean(axis=0)
    return average.astype(int)


def create_image(rgb_color):
    print(rgb_color)
    img = Image.new('RGB', (320, 320), tuple(rgb_color))
    name = f'avg_{time.time()}.png'
    img.save(os.path.join(settings.MEDIA_ROOT, name), 'PNG')
    return name
