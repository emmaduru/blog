from django.urls import path
from .views import PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView

urlpatterns = [
    path("new/", PostCreateView.as_view(), name="create"),
    path("<int:pk>/delete/", PostDeleteView.as_view(), name="delete"),
    path("<int:pk>/detail/", PostDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", PostUpdateView.as_view(), name="edit"),
    path("", PostListView.as_view(), name="home")
]