from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post
from .forms import CommentForm

# Create your views here.

# Starting or Landing Page
class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ['-date']
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3] # It's equal to Post.objects.all()[:3]
        return data

# All Posts Page
class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ['-date']
    context_object_name = "all_posts"

# Single Post
class SinglePostView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post

    # fetching tags data as well
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_tags'] = self.object.tags.all()
        context["comment_form"] = CommentForm()
        return context

def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3] # It will directly just fetch 3 records from DB, not just fetch all and then slice first 3.
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post(request, slug):
    # identified_post = Post.object.get(slug=slug)
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })