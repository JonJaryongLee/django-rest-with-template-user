from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from api.models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.


def index(request):
    return render(request, 'articles/index.html')


def about(request):
    return render(request, 'articles/about.html')


def board(request):
    articles = get_list_or_404(Article)
    content = {
        'articles': articles,
    }
    return render(request, 'articles/board.html', content)


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


def move_create(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save(commit=False)
        article.user = request.user
        form.save()
        return render(request, 'articles/create_success.html')


def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.user:
        article.delete()
        return render(request, 'articles/delete_success.html')
    else:
        return render(request, 'articles/index.html')


def move_update(request, pk):
    form = ArticleForm()
    article = get_object_or_404(Article, pk=pk)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)


def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
        form.save()
        return render(request, 'articles/update_success.html')

def comments_create(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect('articles:detail', article.pk)