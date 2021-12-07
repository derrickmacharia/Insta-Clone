from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt
from django.contrib.auth.models import User
from django.db.models.fields import related

# Create your models here.
class Image(models.Model):
    # title field

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image')
    title = models.CharField(max_length=50)
    caption = models.TextField()
    liked= models.ManyToManyField(User,default=None,blank=True,related_name='liked')
    post_date = models.DateTimeField(auto_now_add=True,null=True)
    

    def __str__(self):
        return self.title

    def save_images(self):
        self.save()

        # delete image
    def delete_image(self):
        self.delete()

    @classmethod
    def get_images_by_user(cls, user):
        images = cls.objects.filter(user=user)
        return images

    def update_images(self, title, caption):
        self.title = title
        self.caption = caption
        self.save()

    @property
    def saved_comments(self):
        return self.comments.all()

    # get all images
    @classmethod
    def get_all_images(cls):
        today = dt.date.today()
        images = Image.objects.all(post_date__date = today)
        return images

    @classmethod
  # search images using image name
    def search_image_name(cls, search_term):
        images = cls.objects.filter(
        title__icontains=search_term)
        return images    

    def _str_(self):
        return self.user.username       

    def _str_(self):
        return self.title
    #  get a single image using id
    @classmethod
    def get_single_image(cls, id):
        image = cls.objects.get(id=id)
        return image

    def _str_(self):
        return self.title
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = CloudinaryField('image')
    bio = models.TextField(max_length=500, blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)

    def update(self):
        self.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile_by_user(cls, user):
        profile = cls.objects.filter(user=user)
        return profile

    

    def __str__(self):
        return self.user.username


LIKE_CHOICES={
    ('Like','Like'),
    ('Unlike','Unlike',)
}
class Likes(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,default='like',max_length=10)

    def _str_(self):
        return self.value
class Follow(models.Model):
    user = models.OneToOneField(User, related_name='following',on_delete = models.CASCADE)
    follower = models.ForeignKey(User, related_name='followers',on_delete = models.CASCADE)

    def __str__(self):
        return "%s follower" % self.follower


class Comment(models.Model):
    comment = models.CharField(max_length=250)
    image = models.ForeignKey(Image,on_delete = models.CASCADE,related_name='comments')
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name='comments')

    @classmethod
    def display_comment(cls,image_id):
        comments = cls.objects.filter(image_id = image_id)
        return comments
