from django.http import HttpResponseRedirect
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Post

def posts(request):
    post = Post.objects.all()
    context = {
        'posts': post,
        'title': 'Projects'
    }
    return (render(request, 'Posts/projects.html', context))


class PostListView(ListView):
    model = Post
    template_name = 'Posts/projects.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 9

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','caption','content','image','link']
    template_name = 'Posts/projects_create.html'
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','caption','content','image','link']
    template_name = 'Posts/projects_create.html'
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user== post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



# Create your views here.
