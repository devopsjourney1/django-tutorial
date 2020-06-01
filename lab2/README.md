# LAB 2
1. Create a folder for POSTS
``` shell
python manage.py startapp posts
```

2. In posts/models.py add in a Post class
``` shell
class Post(models.Model):
    title = models.CharField(max_length=25)
    body = models.CharField(max_length=500)
```

3. Modify blog/settings.py to add Posts as an installed APP


4. Work with the migrations
``` shell
python manage.py makemigrations
python manage.py showmigrations
python manage.py migrate
```

6. Create a Super user for the Django Admin site
``` shell
python manage.py createsuperuser
```

7. Add the post model to posts/admin.py
``` shell
from .models import Post

admin.site.register(Post)
```

8. Add a str repr to the Post model.
``` shell
    def __str__(self):
        return f"{self.title}"
```