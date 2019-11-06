from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Create your models here.

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


    def total_likes(self):
       self.likes.count()

    @classmethod
    def search_by_title(cls,search_term):
        pic = cls.objects.filter(title__icontains=search_term)
        return pic


class Neighborhood(models.Model):
    neighborhood_name=models.CharField(max_length=20)

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls,neighborhood_id):
        neighborhood = cls.objects.get(id=neighborhood_id)
        return neighborhood

    def update_neighborhood(self,name):
        self.name = name
        self.save()


    def __str__(self):
        return f'{self.neighborhood_name}'

    

class Post(models.Model):
    title=models.CharField(max_length=40)
    post_description=models.TextField(max_length=1000000)
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE)
    neighborhoods=models.ForeignKey(Neighborhood)

    def __str__(self):
        return f'{self.title}'




class Business(models.Model):
    business_name=models.CharField(max_length=20)
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE)
    neighborhoods=models.ForeignKey(Neighborhood)
    email_adress=models.EmailField()

    def __str__(self):
        return f'{self.business_name}'



class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
   profile_picture = models.ImageField(upload_to='images/')
   name = models.CharField(max_length=200)
   neighborhoods=models.ForeignKey(Neighborhood)
   def __str__(self):
       return self.name
   @classmethod
   def search_profile(cls, username):
       return cls.objects.filter(name__icontains=username)
   def save_profile(self):
       self.user
   def delete_profile(self):
       self.delete()


