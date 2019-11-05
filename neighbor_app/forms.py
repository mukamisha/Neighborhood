from django import forms
from .models import Image,Profile,Post,Neighborhood


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['']

class ProfileForm(forms.ModelForm):
   class Meta:
       model=Profile
       fields=['bio','profile_picture']
       exclude=['user']

class NeighborhoodForm(ModelForm):
    class Meta:
        model = Neighborhood
        fields = ('neighborhood_name',)

