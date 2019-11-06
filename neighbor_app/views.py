from django.shortcuts import render,redirect
from django.http  import HttpResponse
from . models import Image,Neighborhood,Post,User,Business
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm,ProfileForm,NeighborhoodForm,BusinessForm
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    neighborhood= Neighborhood.objects.all()
    return render(request, 'home.html',{'neighborhood':neighborhood})

   
@login_required(login_url='/accounts/login/')
def neighborhood(request,neighborhood_id):
    
    current_user=request.user
    neighbors= Neighborhood.objects.get(id=neighborhood_id)
    posts=Post.objects.filter(neighborhoods=neighbors.id).all()
    businesseses=Business.objects.filter(neighborhoods=neighbors.id).all()
    return render(request,'neighborhood.html',{'neighbors':neighbors,'neighborhood_id':neighborhood_id,'posts':posts,'businesseses':businesseses})


@login_required(login_url='/accounts/login/')
def new_post(request,neighborhood_id):
    current_user = request.user
    neighbors= Neighborhood.objects.get(id=neighborhood_id)
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.posted_by = current_user
            post.neighborhoods=neighbors
            post.save()
        return redirect('neighborhood', neighborhood_id)

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form, "neighborhood_id": neighborhood_id})
# a view function that adds a business model 

@login_required(login_url='/accounts/login/')
def add_business(request,neighborhood_id):
    current_user = request.user
    neighbors= Neighborhood.objects.get(id=neighborhood_id)
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            biz = form.save(commit=False)
            biz.posted_by = current_user
            biz.neighborhoods=neighbors
            biz.save()
        return redirect('neighborhood', neighborhood_id)

    else:
        form = BusinessForm()
    return render(request, 'new_biz.html', {"form": form, "neighborhood_id": neighborhood_id})

   
@login_required(login_url='/accounts/login/')
def profile(request,neighborhood_id):
    
    current_user=request.user
    profile=Profile.objects.filter(user=current_user).first()
    return render(request,'profile.html',{'neighbors':neighbors,'neighborhood_id':neighborhood_id,'posts':posts,'businesseses':businesseses})

# a function to get the profile
@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user
    if request.method =='POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.posted_by = current_user
            profile.save()
        return redirect('profile')

    else:
        form = ProfileForm()
    return render(request, 'add_profile.html', {"form": form})

    

@login_required(login_url='/accounts/login/')
def profile_edit(request):
   current_user=request.user
   if request.method=='POST':
       form=ProfileForm(request.POST,request.FILES)
       if form.is_valid():
           image=form.save(commit=False)
           image.user=current_user
           image.save()
       return redirect('profile')
   else:
       form=ProfileForm()
   return render(request,'update.html',{"form":form})

@login_required(login_url='/accounts/login/')
def search_picture(request):

    if 'title' in request.GET and request.GET["title"]:
        search_term = request.GET.get("title")
        searched_images = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})











