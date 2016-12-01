from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Titles, Associated_Persons
from django.http import HttpResponse
import datetime
# from .forms import PostForm


def title_list(request):
    titles = Titles.objects.order_by('title')
    return render(request, 'mrdb/title_list.html', {'titles':titles})

def people_list(request):
    name = Associated_Persons.objects.order_by('name')
    return render(request, 'mrdb/people_list.html', {'name':name})
    
def title_detail(request, pk):
    title = get_object_or_404(Titles, pk=pk)
    return render(request, 'mrdb/title_detail.html', {'title': title})

def about(request):
    return render(request, 'mrdb/about.html', {})

def participate(request):
    return render(request, 'mrdb/participate.html', {})
    
def contact(request):
    return render(request, 'mrdb/contact.html', {})

def movies(request):
    return render(request, 'mrdb/movies.html', {})

def tv(request):
    return render(request, 'mrdb/tv.html', {})

def search(request):
    return render(request, 'mrdb/search.html', {})

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)




"""
#    names = Associated_Persons.objects.order_by('name')
#    return render(request, 'mrdb/people_list.html', {'names':name})
    

    people = Associated_Persons.objects.order_by('name')
    return render(request, 'mrdb/people_list.html', {'people':people})
def tv_list(request):
    titles = Titles.objects.order_by('year')
    return render(request, 'mrdb/title_list.html', {'titles':titles})

def movie_list(request):
    titles = Titles.objects.order_by('year')
    return render(request, 'mrdb/title_list.html', {'titles':titles})



#    return HttpResponse("Hello, World")
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

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
    return render(request, 'mrdb/post_edit.html', {'form': form})

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
    return render(request, 'mrdb/post_edit.html', {'form': form})
"""