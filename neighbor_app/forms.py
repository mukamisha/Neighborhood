from django import forms
from .models import Image,Profile,Comment


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['posted_by']

class ProfileForm(forms.ModelForm):
   class Meta:
       model=Profile
       fields=['bio','profile_picture']
       exclude=['user']
       
class CommentForm(forms.ModelForm):
   class Meta:
       model=Comment
       exclude=['comment_pic','posted_by']


