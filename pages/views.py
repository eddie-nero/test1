from django.http.response import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import UploadFile

# from somewhere import handle_uploaded_file


class HomePageView(TemplateView):
    template_name = 'home.html'


def file_upload_view(request):
    # print(request.FILES)
    if request.method == 'POST':
        my_file = request.FILES.get('file')
        UploadFile.objects.create(file=my_file)
        return HttpResponse('')
    return JsonResponse({'post': 'false'})
