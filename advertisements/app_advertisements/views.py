from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Advertisement
from .forms import AdvertisementForm
from django.contrib.auth import get_user_model
from django.db.models import Count

User = get_user_model()

def index(requests):
    title = requests.GET.get('query')
    if title:
        advertisements = Advertisement.objects.filter(title__icontains = title)
    else:
        advertisements = Advertisement.objects.all()
    context = {'advertisements' : advertisements,
               'title' : title,
               }
    return render(requests, 'app_advertisements/index.html', context)

def advertisement_detail(request, pk):
    advertisement = Advertisement.objects.get(id = pk)
    context = {
        'advertisement' : advertisement
    }
    return render(request, 'app_advertisements/advertisement.html', context)

def top_sellers(requests):
    users = User.objects.annotate(
        adv_count = Count('advertisment')
    ).order_by('-adv_count')

    context = { 'users' : users}
    return render (requests, 'app_advertisements/top-sellers.html', context)



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
