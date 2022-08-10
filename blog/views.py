from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.


def post_list(request):
    posts = Post.objects .filter(published_date__lte=timezone.now()).order_by('published_date')
    '''
    - request parameter responsible for displaying everything that received from the internet 
    - template name
    - {} use to add additional value that the template can use 
    '''
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})