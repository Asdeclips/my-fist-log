from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Card
from .forms import PostForm

def post_list(request):
    posts = Card.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'tribute/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Card, pk=pk)
    return render(request, 'tribute/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('tribute.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'tribute/post_edit.html', {'form': form})

def post_edit(request,pk):
    post = get_object_or_404(Card, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('tribute.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'tribute/post_edit.html', {'form': form})