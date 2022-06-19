from django.urls import path

from .import views


urlpatterns = [
    path('post/', views.PostView.as_view()),
    path('create_post/', views.PostCreateView.as_view()),
    path('post/<int:pk>/', views.PostDeteilView.as_view()),

    path('comment/', views.CreateComment.as_view()),
    path('post_deteil_comment/<int:pk>/', views.CommentsOnASpecificPostView.as_view()),
    path('self_comment/<int:pk>/', views.GetNestedComment.as_view()),

    path('like/', views.CreateLikeDislike.as_view())
]
