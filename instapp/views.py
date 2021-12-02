from django.shortcuts import render

from instapp.models import Images

# Create your views here.

def index(request):
    image = Images.objects.all().order_by('-id')

    return render(request, 'all-photos/index.html',{'image': image})
