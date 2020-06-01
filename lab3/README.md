# Lab 3

1. Send the datetime from view to render template
``` shell
from datetime import datetime

{ "current_time": datetime.now(),
  "num_posts": Post.objects.count(),
  "posts" Post.objects.all() }


```

2. Update website/welcome.html to render current_time using Jinja templating
``` shell
Hello! The current time is {{current_time}}.
```



3. Add Post object to view
``` shell
from meetings.models import Meeting, Room

{ "current_time": datetime.now()),
  "num_posts": Post.objects.count(),
  "posts" Post.objects.all() }
```

4. Update website/welcome.html to render the Post data using Jinja 
``` shell

    This blog currently has {{num_posts}} posts.

    {% for post in posts %}
         <h2>{{ post.title }}</h2>
         <p>{{ post.body }}</p>
    {% endfor %}
```

5. Creates base.html in templates folder and add templating to welcome.html

