from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm


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

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.P0ST) #  Construct a form with new data input
#         if form.is_valid():
#             """
#             .save() --> saves the file but commit is set to false as the author needs to be stated before
#             actually proceeding
#             """
#             post = form.save(commit=False)  # save the file
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)  # redirects the save post to the detail page
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})
