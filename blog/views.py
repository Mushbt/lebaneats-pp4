from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, RecipeForm
from django.contrib import messages


def home(request):
    return render(request, "index.html")


def about_us(request):
    return render(request, "about_us.html")

    """
    Add recipe function
    """


def add_recipe(request):
    recipe_form = RecipeForm(request.POST or None, request.FILES or None)
    context = {
        'recipe_form': recipe_form,
    }

    if request.method == "POST":
        recipe_form = RecipeForm(request.POST, request.FILES)
        if recipe_form.is_valid():
            recipe_form = recipe_form.save(commit=False)
            recipe_form.author = request.user
            recipe_form.status = 0
            recipe_form.save()
            messages.success(request, 'Your recipe is awaiting approval')
            return redirect('blog')
        else:
            messages.error(request, 'Invalid, Please try again.')
            return render(request, 'add_recipe.html', context)
    else:
        recipe_form = RecipeForm()
    return render(request, 'add_recipe.html', context)


class PostList(generic.ListView):
    """
    Creates the post list
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'
    paginate_by = 6


class PostDetail(View):
    """
    Creates the post detail
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
                "recipe_form": RecipeForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Your comment is awaiting approval')
        else:
            messages.error(request, 'Invalid, Please try again.')
            comment = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )


def edit_recipe(request, slug):
    post = get_object_or_404(Post, slug=slug)
    recipe_form = RecipeForm(request.POST or None, instance=post)

    context = {
        "recipe_form": recipe_form,
        "post": post,
    }
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST, request.FILES, instance=post)
        if recipe_form.is_valid():
            post = recipe_form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'You successfully updated your recipe')
            return redirect('blog')

        else:
            recipe_form = RecipeForm(instance=post)
    return render(request, "edit_recipe.html", context)


def delete_recipe(request, slug):
    post = Post.objects.get(slug=slug)
    post.delete()
    messages.success(request, 'You successfully deleted your recipe')
    return redirect('blog')


class PostLike(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
