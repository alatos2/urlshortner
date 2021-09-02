from django.shortcuts import render, redirect

from django.http import HttpResponse

from django import forms

import uuid as myuuid

from .models import Url

# Create your classes here
class UrlForm(forms.Form):
    url = forms.CharField(label='Url')

# Create your views here.
def index(request):
    return render(request, 'shortner/index.html', {
        'form': UrlForm()
    })

def create(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            uuid = str(myuuid.uuid4())[:5]

            new_url = Url(url=url, uuid=uuid)
            new_url.save()
            return render(request, 'shortner/index.html', {
                'form': UrlForm(),
                'uuid': 'http://localhost:8000/'+uuid
            })

def go(request, pk):
    link = Url.objects.get(uuid=pk)
    return redirect(link.url)