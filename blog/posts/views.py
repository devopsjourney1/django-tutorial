from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post
from django.contrib import messages

# Create your views here.

def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, "posts/detail.html", {"post": post })

@login_required()
def delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    messages.warning(request, f'Post deleted!')
    return redirect("/")

@login_required()
def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Post Created!')
            return redirect("/")
    else:
        form = PostForm()
    return render(request, "posts/new.html", {"form": form })
