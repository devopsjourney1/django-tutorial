
# Lab 4
1. Import BootStrap and FontAwesome
``` shell
  <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
  <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">
  <link rel="shortcut icon" href="{% static 'website/favicon.ico' %}" />
```

2. Wrap forloop around new Bootstrap/Div elements in welcome.html
``` shell
{% block content %}
  {% for post in posts %}
    <div class="container">
        <div class="card-deck mb-3 text-center">
        <div class="card mb-4 box-shadow">
            <div class="card-header">
            <h4 class="my-0 font-weight-normal"> </h4>
            </div>
            <div class="card-body">
              <p></p>
            </div>
        </div>
    </div>
  {% endfor %}
{% endblock %}
```

3. Create 'top-menu.html' and include it in your base HTML
``` shell
{% load static %}
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#"><img src="" alt="My image" width="75"></a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
    <div class="navbar-nav">
      <a class="nav-item nav-link active" href="#"><i class="fa fa-home"></i> Home <span class="sr-only">(current)</span></a>
      <a class="nav-item nav-link" href="#"><i class="fa fa-wrench"></i> Features</a>
      <a class="nav-item nav-link" href="#"><i class="fa fa-money"></i> Pricing</a>
      <a class="nav-item nav-link" href ="https://www.youtube.com/channel/UC4Snw5yrSDMXys31I18U3gg"><i class="fa fa-youtube"></i></a>
    </div>
  </div>
</nav>>
</nav>

```
4. Load topmenu into your base.html
``` shell
{% include 'top-menu.html' %}
```



5. Import static files, favicon etc.

