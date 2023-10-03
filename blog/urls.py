from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('share_recipe/', views.add_recipe, name="add_recipe"),
    path('edit_recipe/<slug:slug>', views.edit_recipe, name="edit_recipe"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
