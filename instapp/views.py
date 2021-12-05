from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from instapp.models import Image,Profile
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.shortcuts import render, redirect

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
    return render(request, 'profile.html', {"image": image, "profile": profile})

@login_required(login_url='/accounts/login/')
def save_image(request):
    if request.method == 'POST':
        title = request.POST['title']
        caption = request.POST['caption']
        image_file = request.FILES['image_file']
        image_file = cloudinary.uploader.upload(image_file)
        image_url = image_file['url']
        image_public_id = image_file['public_id']
        image = Image(title=title, caption=caption, image=image_url,
                      profile_id=request.POST['user_id'], user_id=request.POST['user_id'])
        image.save_image()
        return redirect('/profile', {'success': 'Image Uploaded Successfully'})
        # return render(request, 'profile.html', {'success': 'Image Uploaded Successfully'})
    else:
        return render(request, 'profile.html', {'danger': 'Image Upload Failed'})