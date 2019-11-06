from django import forms
from .models import Image,Profile,Post,Neighborhood


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['posted_by','neighborhoods']

class ProfileForm(forms.ModelForm):
   class Meta:
       model=Profile
       fields=['bio','profile_picture']
       exclude=['user']

class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields = ('neighborhood_name',)

