from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Image,Category,Location

# Create your views here.
# def welcome(request):

#     return HttpResponse('Welcome to the Moringa Tribune')


def images(request):
   image = Image.objects.all()

   return render(request, 'image.html',{'image':image})

def search_results(request):

    if 'img' in request.GET and request.GET["img"]:
        search_term = request.GET.get("img")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"searched_images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def get_image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"photo.html", {"image":image})


def filter_by_location(request, id):
   location = Location.objects.all()
   images = Image.objects.filter(location__id=id)
   return render(request, "location.html",{'images':images,'location':location})