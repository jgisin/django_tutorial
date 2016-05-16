from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post

def posts_create(request):

  return HttpResponse("<h1>Create</h1>")

def posts_detail(request):
  instance = get_object_or_404(Post, id=1)
  context = {
      "post": instance
      }
  return render(request, "detail.html", context)

def posts_list(request):
  queryset = Post.objects.all()
  context = {
      "posts": queryset
      }
  return render(request, "index.html", context)

def posts_update(request):

  return HttpResponse("<h1>Update</h1>")

def posts_delete(request):

  return HttpResponse("<h1>Delete</h1>")

