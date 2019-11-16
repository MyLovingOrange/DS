from django.shortcuts import render,render_to_response,redirect
import simplejson
import time
import Crypto.Hash.SHA256 as SHA256
from django.urls import reverse
def index(request):
    return render(request,'index.html')


def toSHA256(request):
    text = request.POST.get('textToSHA')
    SHA256Text = SHA256.new(text.encode('utf8')).hexdigest()
    reInfo = {'SHA256Text': SHA256Text}
    print(reInfo)
    return render(request, 'index.html', reInfo)
