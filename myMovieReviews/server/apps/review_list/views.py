import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from server.apps.review_list.models import Movie
from django.shortcuts import render, redirect


def movie_list(request, *args, **kwargs):
    # text = request.GET.get("text")
    posts = Movie.objects.all()
    
    # if text:
    #     posts = posts.filter(content__contains=text)
    # 주석처리한 부분은 검색기능 구현!
    return render(request, "review_list/movie_list.html", {"posts": posts})

def movie_create(request, *args, **kwargs):
    if request.method == "POST":
        Movie.objects.create(
            title=request.POST["title"],
            director=request.POST["director"],
            release_year=request.POST["release_year"],
            main_actor=request.POST["main_actor"],
            genre=request.POST["genre"],
            score=request.POST["score"],
            running_time=request.POST["running_time"],
            content=request.POST["content"],
        )
        return redirect("/")
    return render(request, "review_list/movie_create.html")

def movie_read(request, pk, *args, **kwargs):
    post = Movie.objects.all().get(id=pk)
    return render(request, "review_list/movie_read.html", {"post": post})

def movie_update(request, pk, *args, **kwargs):
    post = Movie.objects.get(id=pk)

    if request.method == "POST":
        post.title=request.POST["title"]
        post.director=request.POST["director"]
        post.release_year=request.POST["release_year"]
        post.main_actor=request.POST["main_actor"]
        post.genre=request.POST["genre"]
        post.score=request.POST["score"]
        post.running_time=request.POST["running_time"]
        post.content=request.POST["content"]
        post.save()
        return redirect(f"/movie/{post.id}")

    return render(request, "review_list/movie_update.html", {"post" : post})

def movie_delete(request, pk, *args, **kwargs):
    if request.method == 'POST':
        post = Movie.objects.get(id=pk)
        post.delete()
    return redirect("/")
