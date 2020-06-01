from django.urls import path
from . import views

#'http://example.com/posts/'
#'http://example.com/posts/new'
#'http://example.com/posts/1'
#'http://example.com/posts/detele/67856578587'

urlpatterns = [
    path('new', views.new, name='new'),
    path('<int:id>', views.detail, name='detail'),
    path('delete/<int:id>', views.delete, name='delete'),
]