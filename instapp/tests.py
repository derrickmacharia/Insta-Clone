from django.test import TestCase

# Create your tests here.
from django.test import TestCase

from instapp.models import Image, Profile,User

class ImageTestCase(TestCase):
    def setUp(self):
        # create a user
        user = User.objects.create(
            username='test_user',
           
        )
        Image.objects.create(
            title='test_image',
            image='https://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Kenya.svg',
            caption='test image',
            
            user_id=user.id
        )

    def test_image_name(self):
        image = Image.objects.get(title='test_image')
        self.assertEqual(image.title, 'test_image')

    def test_image_id(self):
        user = User.objects.create(
            username='newuser',
            
        )
        photo = Image.objects.create(
            caption='test post',
            image='https://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Kenya.svg',
            
            user_id=user.id
        )

    def test_image_posted_at(self):
        user = User.objects.create(
            username='newuser',
            
        )
        photo = Image.objects.create(
            caption='test post',
            image='https://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Kenya.svg',
            
            user_id=user.id
        )

    def test_image_user(self):
        user = User.objects.create(
            username='newuser',
            
        )
        photo = Image.objects.create(
            caption='test post',
            image='https://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Kenya.svg',
            
            user_id=user.id
        )
    def test_image_photo_caption(self):
        user = User.objects.create(
            username='newuser',
            
        )
        photo = Image.objects.create(
            caption='test post',
            image='https://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Kenya.svg',
            
            user_id=user.id
        )
    def test_image_liked(self):
        user = User.objects.create(
            username='newuser',
            
        )
        photo = Image.objects.create(
            caption='test post',
            image='https://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Kenya.svg',
            
            user_id=user.id
        )
