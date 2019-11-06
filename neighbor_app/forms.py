from django import forms
from .models import Image,Profile,Post,Neighborhood,Business


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['posted_by','neighborhoods']

class ProfileForm(forms.ModelForm):
   class Meta:
       model=Profile
       fields=['name']
       exclude=['user']

class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields = ['neighborhood_name']
class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        exclude=['posted_by','neighborhoods']
           

