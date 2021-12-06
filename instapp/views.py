from django import forms
from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from instapp.models import Image,Profile,Likes
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.shortcuts import render, redirect
from .forms import PostImageForm,CommentForm

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    image = Image.objects.all().order_by('-id')

    return render(request, 'all-photos/index.html',{'image': image})



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

# def post_detail(request, slug):
#     template_name = 'post_detail.html'
#     post = get_object_or_404(Image, slug=slug)
#     comments = post.comments.filter(active=True)
#     new_comment = None
#     # Comment posted
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():

#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.post = post
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm()

#     return render(request, template_name, {'post': post,'comments': comments,'new_comment': new_comment,'comment_form': comment_form})
