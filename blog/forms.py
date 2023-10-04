from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'title',
            'recipe_difficulty',
            'recipe_length',
            'ingredients',
            'instructions',
        ]

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)

    def recipe_length(self):
        value = self.cleaned_data.get("length")
        print(value)
        if value < 1:
            raise forms.ValidationError(
                "The recipe length must be greater than zero"
            )
        return value
