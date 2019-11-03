from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Image
class TestProfile(TestCase):
   def setUp(self):
       self.user = User(username='jacky')
       self.user.save()
       self.profile_test = Profile( profile_picture='624244.jpg', bio='engeneer', user=self.user)
   def test_instance(self):
       self.assertTrue(isinstance(self.profile_test, Profile))
   def test_save_profile(self):
       self.profile_test.save_profile()
       travel = Profile.objects.all()
   def tearDown(self):
       Profile.objects.all().delete()

class TestImage(TestCase):
   def setUp(self):
       self.profile_test = Profile()
       self.profile_test.save()
       self.image_test = Image(image='insta.png', image_name='goodgirl', caption='i like her', profile=self.profile_test)
   def test_instance(self):
       self.assertTrue(isinstance(self.image_test, Post))
   def test_save_image(self):
       self.image_test.save_image()
       images = Post.objects.all()
       self.assertTrue(len(images) > 0)
   def tearDown(self):
       Image.objects.all().delete()
   def test_delete_image(self):
     
       self.images.save_image()
       self.image = Image.objects.get(id = 1)
       self.image.delete_image()
       self.assertTrue(len(Image.objects.all()) == 0)