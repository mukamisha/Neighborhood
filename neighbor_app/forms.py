from django import forms
from .models import Image,Profile,Comment


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile','comments']

class ProfileForm(forms.ModelForm):
   class Meta:
       model=Profile
       fields=['bio','profile_picture']
       exclude=['user']
       
class CommentForm(forms.ModelForm):
   class Meta:
       model=Comment
       exclude=['comment_pic','posted_by']

