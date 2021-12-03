from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt

# Create your models here.
class Images(models.Model):
    # title field
    image = CloudinaryField('image')
    title = models.CharField(max_length=50)
    caption = models.TextField(max_length=1500)
    post_date = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return self.title

    def save_images(self):
        self.save()

    def update_images(self, title, caption):
        self.title = title
        self.caption = caption
        self.save()

    # get all images
    @classmethod
    def get_all_images(cls):
        today = dt.date.today()
        images = Images.objects.all(post_date__date = today)
        return images

    