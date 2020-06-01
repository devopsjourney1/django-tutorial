
# Lab 7


# users can be created by using python manage.py createsuperuser

1. Configure URLS
``` shell
path('accounts/', include('django.contrib.auth.urls')),

#The urls provided by this are
#accounts/login/ [name='login']
#accounts/logout/ [name='logout']
#accounts/password_change/ [name='password_change']
#accounts/password_change/done/ [name='password_change_done']
#accounts/password_reset/ [name='password_reset']
#accounts/password_reset/done/ [name='password_reset_done']
#accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
#accounts/reset/done/ [name='password_reset_complete']

```


2. Add Login/Logout functionality
``` shell
      {% if user.is_authenticated %}
        <a class="btn btn-outline-danger my-2 my-sm-0" href="{% url 'login' %}">Logout</a> 
         {{ user.username }}
      {% else %}
        <a class="btn btn-outline-success my-2 my-sm-0" href="{% url 'login' %}">Login</a>
      {% endif %}
```


3. Create Login template: registration/login.html
``` shell
{% extends 'base.html' %}

{% block title %}Login{% endblock %}

{% block content %}
  <h2>Login</h2>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Login</button>
  </form>
{% endblock %}
```



4. Add login redirect to settings
``` shell
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
```

5. Add author to posts/models.py
``` shell
author = models.ForeignKey(User, on_delete=models.CASCADE)
```

6. Get user id of your user
``` shell
python .\manage.py dbshell
.tables
select id,username from 
```

7. Make and run a migration
``` shell
python .\manage.py makemigrations
python .\manage.py migrate
```

8. Create a post.html and convert detail.html and welcome.html to include it. this way we are only changing one template 
``` shell
{% include 'posts/post.html'%}

```


9. Add exclusion in forms
``` shell
        exclude = ('author',)
```

10. Add decorater to posts/views.py to make it so a login is required
``` shell
from django.contrib.auth.decorators import login_required
@login_required()
```

11. Create a create user page
``` shell
django.contrib.auth.forms import UserCreationForm

```

12. Add a Create user button to top-menu.html
``` shell

```