from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from instapp.models import Images

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    image = Images.objects.all().order_by('-id')

    return render(request, 'all-photos/index.html',{'image': image})
