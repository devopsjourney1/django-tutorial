from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post

# Create your views here.

def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, "posts/detail.html", {"post": post })
    
def delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect("/")

def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = PostForm()
    return render(request, "posts/new.html", {"form": form })
