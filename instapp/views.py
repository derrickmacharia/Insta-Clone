from django import forms
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from instapp.models import Image,Profile
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.shortcuts import render, redirect
from .forms import PostImageForm

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    image = Image.objects.all().order_by('-id')

    return render(request, 'all-photos/index.html',{'image': image})


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    # get images for the current logged in user
    image = Image.objects.filter(user_id=current_user.id)
    # get the profile of the current logged in user
    profile = Profile.objects.filter(user_id=current_user.id).first()

    form = PostImageForm()

    context = {"image": image, "profile": profile, "form": form}
    if request.method == 'POST':
        form = PostImageForm (request.POST , request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
        redirect('profile')


        

    return render(request, 'profile.html',context)


