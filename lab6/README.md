
# Lab 6
1. Create a details function
``` shell
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

def detail(request, id):
    #post = Post.objects.get(pk=id)
    post = get_object_or_404(Post, pk=id)
    return render(request, "posts/detail.html", {"post": post})

def delete(request, id):
    #post = Post.objects.get(pk=id)
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect("/")


```


2. Change blog/urls.py to bring in all urls for posts
``` shell
from django.urls import path, include

path('posts/', include('posts.urls')),
```

3. Move URL pattern to posts/urls.py
``` shell
from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.detail, name='detail'),
    path('<int:id>', views.delete, name='delete'),
    path('new', views.new, name='new'),
]
```

4. Create a template for posts/detail.html
``` shell


# Also give the name to welcome/home path in the url patterns
    path('', welcome, name='home'),

```

5. Add a url to to get to post details. Also start using url tags templating for top-menu
``` shell
{% url 'detail' post.id %}
{% url 'delete' post.id %}
```




{% extends "base.html" %}
{% block title %}Post - {{post.title}} {% endblock %}
{% block content %}

    <div class="container">
        <div class="card-deck mb-3 text-center">
        <div class="card mb-4 box-shadow">
            <div class="card-header">
            <h4 class="my-0 font-weight-normal">{{post.title}} </h4>
            </div>
            <div class="card-body">
              <p>{{post.body}}</p>
            </div>
        </div>
    </div>

{% endblock %}

<p><a href="{% url 'delete' post.id %}" class="btn btn-danger btn-sm">Delete Post</a></p>
<a href="{% url 'home' %}">Home</a>

{% endblock %}