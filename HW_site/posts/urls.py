from django.urls import path
from .views import CreatePostView, AllPostsView, DeletePost, PostUpdate, VIewPost


urlpatterns = [
    path('posts/', AllPostsView.as_view(), name='all_posts'),
    path('create/', CreatePostView.as_view(), name='create_post'),
    path('delete/<int:post_id>/', DeletePost.as_view(), name='delete_post'),
    path('update/<int:post_id>/', PostUpdate.as_view(), name='update_post'),
    path('view/<int:post_id>/', VIewPost.as_view(), name='view_post')
    # path('comment/', CreateComment.as_view(), name='comment')
]

