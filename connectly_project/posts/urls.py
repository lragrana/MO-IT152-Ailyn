from django.urls import path
from . import views



# urlpatterns = [
#     path('users/', views.get_users, name='get_users'),
#     path('users/create/', views.create_user, name='create_user'),
#     path('posts/', views.get_posts, name='get_posts'),
#     path('posts/create/', views.create_post, name='create_post'),
# ]

urlpatterns = [
    path('log/', views.LoginView.as_view(), name='user-list-create'),
    path('users/', views.UserListCreate.as_view(), name='user-list-create'),
    path('posts/', views.PostListCreate.as_view(), name='post-list-create'),
    path('comments/', views.CommentListCreate.as_view(), name='comment-list-create'),
]

