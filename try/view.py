from django.http import HttpResponse
from django.shortcuts import render
from pytube import *
from tkinter.filedialog import *

def index(request):
    return render(request,'index.html')

def analize(request):
    djtext = request.POST.get('text','default')
    url=YouTube(djtext)
    path = askdirectory()
    strms=url.streams.get_highest_resolution()
    strms.download(path,filename="aa")
    return render(request,'analize.html')