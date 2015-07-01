from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from blog.models import Blog
from blog.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

def index(request):
    return render(request,'blog/index.html')
