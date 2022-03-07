from django.shortcuts import render
from django.views.generic import ListView,DetailView
from blog.models import Post
from django.core.exceptions import PermissionDenied

# Create your views here.



class PostList(ListView): #ListViewはオブジェクトをリスト表示するための機能を提供する
    model=Post
    context_object_name="posts"

class PostDetail(DetailView):
    model=Post
    context_object_name="post"

    def get_object(self):
        post = super().get_object()
        if post.is_published or self.request.user.is_authenticated:
            return post
        else:
            raise PermissionDenied
