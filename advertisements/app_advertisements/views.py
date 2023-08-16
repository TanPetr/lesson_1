from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Advertisement
from .forms import AdvertisementForm

def index(requests):
    advertisements = Advertisement.objects.all()
    context = {'advertisements' : advertisements}
    return render(requests, 'index.html', context)

def top_sellers(requests):
    return render (requests, 'top-sellers.html')

def register(requests):
    return render (requests, 'register.html')

def login(requests):
    return render (requests, 'login.html')

def profile(requests):
    return render (requests, 'profile.html')

def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()

    context = {'form' : form}
    return render (request, 'advertisement-post.html', context)

# Create your views here.
