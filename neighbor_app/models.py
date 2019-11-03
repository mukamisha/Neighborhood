from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()  

    def delete_location(self):
        self.delete() 

    def update_location(self):
        self.update() 

class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name 

    def save_category(self):
        self.save()

    def update_category(self):
        self.update()
    def delete_category(self):
        self.delete()


class Image(models.Model):
    img =  models.ImageField(upload_to = 'image/')
    img_name = models.CharField(max_length =30)
    img_description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category,db_column='name')
  
    def __str__(self):
        return self.img_name

    @classmethod
    def search_by_category(cls,search_term):
        news = cls.objects.filter(category__name__icontains=search_term)
        return news