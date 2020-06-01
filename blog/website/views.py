from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from posts.models import Post
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def welcome(request):
    return render(request, "website/welcome.html",
                  {"current_time": datetime.now(),
                   "posts": Post.objects.all(),
                   "num_posts": Post.objects.count()})
    
def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            new_user = authenticate(username=username, 
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            messages.success(request, f'Account created for {username}')
            return redirect("/")
    else:
        form = UserRegisterForm()
    return render(request, "registration/signup.html", {"form": form})



# def new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/")
#     else:
#         form = PostForm()
#     return render(request, "posts/new.html", {"form": form })
