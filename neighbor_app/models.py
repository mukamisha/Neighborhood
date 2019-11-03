from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
   profile_picture = models.ImageField(upload_to='images/')
   bio = models.TextField(max_length=700)
   name = models.CharField(max_length=200)
   
   def __str__(self):
       return self.name
   @classmethod
   def search_profile(cls, username):
       return cls.objects.filter(name__icontains=username)
   def save_profile(self):
       self.user
   def delete_profile(self):
       self.delete()

class Image(models.Model):
    image= models.ImageField(upload_to = 'image/')
    title = models.CharField(max_length =30)
    description = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
   

    def __str__(self):
        return self.title

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()

    @classmethod
    def get_all_images(cls):
       images=cls.objects.all().prefetch_related('comment_set')
       return images

    def total_likes(self):
       self.likes.count()

    @classmethod
    def search_by_title(cls,search_term):
        pic = cls.objects.filter(title__icontains=search_term)
        return pic

class Comment(models.Model):
   posted_by=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
   comment_pic=models.ForeignKey(Image,on_delete=models.CASCADE,null=True)
   comment=models.CharField(max_length=20,null=True)
   def __str__(self):
       return self.posted_by

class Neighborhood(models.Model):
    neighborhood_name=models.CharField(max_length=20)
    def __str__(self):
        return f'{self.neighborhood_name}'



