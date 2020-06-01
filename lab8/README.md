# Lab 8
# users can be created by using python manage.py createsuperuser

1. Add button for signup
``` shell
<a class="btn btn-outline-info my-2 my-sm-0" href="{% url 'signup' %}">Sign up</a>
```

2. Add the url for signup
``` shell
from website.views import welcome, signup
    path('accounts/signup', signup, name=signup),
```
3. Add the function signup to website\view.py
``` shell
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
```
