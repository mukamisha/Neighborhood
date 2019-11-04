from django.shortcuts import render,redirect
from django.http  import HttpResponse
from . models import Image,Neighborhood
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm,ProfileForm,CommentForm

# Create your views here.

@login_required(login_url='/accounts/login/')
def neighborhood(request,):
    neighbor= Neighborhood.objects.all()
    return render(request, 'home.html',{'Images':neighbor})

# @login_required(login_url='/accounts/login/')
# def images(request,):
#     image= Image.objects.all()
#     return render(request, 'home.html',{'images':image})


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('image')

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
def comment(request,image_id):
   current_user=request.user
   if request.method=='POST':
       image_detail=Image.objects.filter(id=image_id).first()

       form=CommentForm(request.POST,request.FILES)
       if form.is_valid():
           comment=form.save(commit=False)
           comment.posted_by=current_user
           comment.comment_pic=image_detail
           comment.save()
       return redirect('image')
   else:
       form=CommentForm()
   return render(request,'comment.html',{"form":form,"image_id":image_id})

@login_required(login_url='/accounts/login/')
def rate(request,image_id):

       rate = Image.objects.filter(id=image_id).first()
       average_score = round(((rate.design + rate.usability + rate.content)/3),2)
       if request.method == 'POST':
           rate_form = RateForm(request.POST)
           if rate_form.is_valid():
               rate.vote_submissions+=1
               if rate.design == 0:
                   rate.design = int(request.POST['design'])
               else:
                   rate.design = (rate.design + int(request.POST['design']))/2
               if rate.usability == 0:
                   rate.usability = int(request.POST['usability'])
               else:
                   rate.usability = (rate.usability + int(request.POST['usability']))/2
               if rate.content == 0:
                   rate.content = int(request.POST['content'])
               else:
                   rate.content = (rate.content + int(request.POST['usability']))/2
               rate.save()
               return redirect('rate', image_id)
       else:
           rate_form = RateForm()

           return render(request,'rate.html',{"rate_form":rate_form,"rate":rate,"average_score":average_score})


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









