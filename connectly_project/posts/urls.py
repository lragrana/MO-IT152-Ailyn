from django.urls import include, path
from . import views



# urlpatterns = [
#     path('users/', views.get_users, name='get_users'),
#     path('users/create/', views.create_user, name='create_user'),
#     path('posts/', views.get_posts, name='get_posts'),
#     path('posts/create/', views.create_post, name='create_post'),
# ]

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('users/', views.UserListCreate.as_view(), name='user-list-create'),
    path('posts/', views.PostListCreate.as_view(), name='post-list-create'),
    path('posts/<int:post_id>/like/', views.LikePost.as_view(), name='like-post'),
    path('posts/<int:post_id>/comments/', views.CommentListCreate.as_view(), name='post-comments'),
    # path('auth/google/login/', views.GoogleLogin.as_view(), name='google_login'),
    # path('auth/', include('dj_rest_auth.urls')),  # Handles login, logout, password reset
    # path('auth/registration/', include('dj_rest_auth.registration.urls')),  # Handles user registration
]


