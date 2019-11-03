from django.test import TestCase
from .models import Location,Category,Image
# Create your tests here.


class LocationTestClass(TestCase):
    # Set up method that helps to create an instance of a class
    def setUp(self):
        self.keke= Location(name='kakiru')


    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.keke,Location))

    # Testing Save Method
    def test_save_method(self):
        self.keke.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

    def tearDown(self):
       '''
       Test delete location behaivour
       '''
       Location.objects.all().delete()
       
    def test_delete_location(self):
       '''
       Test if location can be deleted from db.
       '''
       self.keke.save_location()
       self.location = Location.objects.get(id = 1)
       self.location.delete_location()
       self.assertTrue(len(Location.objects.all()) == 0)


class CategoryTestClass(TestCase):
    # Set up method that helps to create an instance of a class
    def setUp(self):
        self.lili= Category(name='remembrance')


    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.lili,Category))

    def test_save_method(self):
        self.lili.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)


    def tearDown(self):
       '''
       Test delete category behaivour
       '''
       Category.objects.all().delete()

    def test_delete_category(self):
       '''
       Test if category can be deleted from db.
       '''
       self.lili.save_category()
       self.category = Category.objects.get(id = 1)
       self.category.delete_category()
       self.assertTrue(len(Category.objects.all()) == 0)

 
class ImageTestClass(TestCase):

   def setUp(self):
        # Creating a new location and saving it
        self.keke= Location(name = 'kakiru')
        self.keke.save_location()

        # Creating a new category and saving it
        self.lili = Category(name = 'remembrance')
        self.lili.save()

        self.image= Image(img_name = 'passport',img_description = 'This is a random test Photo',location = self.keke)
        self.image.save()

        self.image.category.add(self.category)
