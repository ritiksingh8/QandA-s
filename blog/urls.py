from django.contrib import admin
from django.urls import path, include
from .views import QnAListView, QnADetailView, PostCreateView, AnswerCreateView
from . import views

urlpatterns = [
    # path('', views.home, name='blog-home'),
    path('', QnAListView.as_view(), name='blog-home'),
    path('question/<int:pk>/', QnADetailView.as_view(), name='question-detail'),
    path('blog/', views.about, name='blog-about'),
    path('question/create/',PostCreateView.as_view(),name='post-create'),
    path('question/<int:pk>/answer',AnswerCreateView.as_view(),name='answer-create')
    # path('blog/',include('blog.urls'))

]
