from django import forms
from .models import Topic, Posts


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 5, 'placeholder': 'what is in your mind?'}
    ), max_length=4000, help_text="The max length is 4000", required=True)

    class Meta:
        model = Topic
        fields = ['subject', 'message']


class PostForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ['comment']
