from django.shortcuts import render,redirect
from django.http  import HttpResponse
from . models import Image,Neighborhood,Post,User
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm,ProfileForm,NeighborhoodForm

# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    if not request.user.is_authenticated:
        return redirect('signout')
    else:
        if request.user.id == 1:
            if request.method == 'POST':
                form = NeighborhoodForm(request.POST)
                if form.is_valid():
                    neighborhood = Neighborhood(neighborhood_name=request.POST['neighborhood_name'],neighborhood_location=request.POST['neighborhood_location'])
                    neighborhood.save()
                return redirect('index')
            else:
                form = NeighborhoodForm()
            neighborhoods = Neighborhood.objects.all()
            return render(request,'home.html',{'neighborhoods':neighborhoods,'form':form})




@login_required(login_url='/accounts/login/')
def neighborhood(request,neighborhood_id):
    
    current_user=request.user
    neighbors= Neighborhood.objects.get(id=neighborhood_id)
    # print(neighbors)
    # biz=BusinessClass.objects.filter(neighborhood=neighbors.id).all()
    posts=Post.objects.filter(title=neighbors.id).all()
    # profile=Profile.objects.filter(id=current_user.id).first()
    # return render(request,'neighborhood.html',{'business':biz,'neighbors':neighbors,'neighborhood_id':neighborhood_id})
    return render(request,'neighborhood.html',{'neighbors':neighbors,'neighborhood_id':neighborhood_id,'posts':posts})
@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('index')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})


@login_required(login_url='/accounts/login/')
def profile(request, username=None):
    current_user = request.user
    pictures = Image.objects.filter(user=current_user)
    return render(request,"profile.html",locals(),{"pictures":pictures})

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











