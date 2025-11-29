from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<slug:slug>/like/', views.ToggleLikeView.as_view(), name='toggle_like'),
    path('tag/<slug:tag_slug>/', views.PostByTagView.as_view(), name='post_by_tag'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
]