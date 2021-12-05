from django import forms
from django.db.models import fields
from instapp.models import Image,Profile

class PostImageForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={

        'id': 'imageform', 'class': 'uploadimage'

    }))

    class Meta:
        model = Image
        fields = ['image','title','caption']
