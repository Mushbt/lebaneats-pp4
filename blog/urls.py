from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('blog', views.PostList.as_view(), name='blog'),
    path('about_us/', views.about_us, name='about_us'),
    path('add_recipe/', views.add_recipe, name="add_recipe"),
    path('edit_recipe/<slug:slug>', views.edit_recipe, name="edit_recipe"),
    path('delete_recipe/<slug:slug>', views.delete_recipe,
         name="delete_recipe"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
