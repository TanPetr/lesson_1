from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Advertisement
from .forms import AdvertisementForm

def index(requests):
    advertisements = Advertisement.objects.all()
    context = {'advertisements' : advertisements}
    return render(requests, 'app_advertisements/index.html', context)

def top_sellers(requests):
    return render (requests, 'app_advertisements/top-sellers.html')



def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            new_advertisement = form.save(commit=False)
            new_advertisement.user = request.user
            new_advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()

    context = {'form' : form}
    return render (request, 'app_advertisements/advertisement-post.html', context)

# Create your views here.
