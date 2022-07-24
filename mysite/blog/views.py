from django.shortcuts import render,get_object_or_404
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    # posts2 = Post.publish.all()
    print(posts)
    return render(request, 'blog/post/list.html',context={'posts':posts})

def post_detail(request,year,month,day,post):

    post = get_object_or_404(Post,slug=post,status='published',published__year = year,published__month = month, published__day = day)

    return render(request,'blog/post/detail.html',context={'post':post})