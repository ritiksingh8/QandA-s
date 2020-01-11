from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Answer

# Create your views here.


def home(request):

    return render(request, 'blog/home.html', context={'posts': Post.objects.all(),
                                                      'answers': Answer.objects.all()
                                                      })


def about(request):

    return render(request, 'blog/about.html')


class QnAListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['answers'] = Answer.objects.all()
        return context


class QnADetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['answers'] = Answer.objects.all()
        ordering = ['-date_posted']
        return context
