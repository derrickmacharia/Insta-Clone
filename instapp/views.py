from django import forms
from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from instapp.models import Image,Profile,Likes,Comment
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import PostImageForm,CommentForm

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    image = Image.objects.all().order_by('-id')
    user = Profile.objects.all()
    
    if request.method == 'POST':  
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            com = form.save(commit=False)
            com.user = request.user
            com.save()
            return redirect('index')
    
    else:
        form = CommentForm()

    return render(request, 'all-photos/index.html',{'image': image, 'form': form, 'user': user})



@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    image = Image.objects.filter(user_id=current_user.id)
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

@login_required(login_url='/accounts/login/')
def search_post(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search').lower()
        images = Image.search_image_name(search_term)
        message = f'{search_term}'

        return render(request, 'all-photos/search.html', {'found': message, 'images': images})
    else:
        message = 'Not found'
        return render(request, 'all-photos/search.html', {'danger': message})

# @login_required(login_url='/accounts/login/')
# def user_profile(request, id):
#     # check if user exists
#     if User.objects.filter(id=id).exists():
#         # get the user
#         user = User.objects.get(id=id)
#         # get all the images for the user
#         image = Image.objects.filter(user_id=id)
#         # get the profile of the user
#         profile = Profile.objects.filter(user_id=id).first()
#         return render(request, 'user-profile.html', {'post': image, 'profile': profile, 'user': user})
#     else:
#         return redirect('/') 

@login_required(login_url='/accounts/login/')
def user_profile(request, user_id):
    prof_user = Profile.objects.filter(user_id=user_id).first()
    images = Image.objects.filter(user_id = user_id)

    return render(request, 'user-prof.html', {'images':images, 'prof_user': prof_user})

def like_image(request):
    user = request.user
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        image_pic =Image.objects.get(id=image_id)
        if user in image_pic.liked.all():
            image_pic.liked.add(user)
        else:
            image_pic.liked.add(user)    
            
        like,created =Likes.objects.get_or_create(user=user, image_id=image_id)
        if not created:
            if like.value =='Like':
               like.value = 'Unlike'
        else:
               like.value = 'Like'

        like.save()       
    return redirect('index')

def single_pic(request,id):

    image = Image.objects.get(id = id)
    related_images = Image.objects.filter(
        user_id=image.user_id).order_by('-image_date')
    imagetitle = image.title

    return render(request, 'pic.html', {'image': image,'images': related_images, 'title': imagetitle})


@login_required
def comments(request,image_id):
  form = CommentForm()
  image = Image.objects.filter(pk = image_id).first()
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit = False)
      comment.user = request.user
      comment.image = image
      comment.save() 
  return redirect('index')

