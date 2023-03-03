from django import forms
from .models import Category


class PostForm(forms.Form):
    title = forms.CharField(max_length=255)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None)
    content = forms.CharField(widget=forms.Textarea(attrs={'id': 'post_content'}))

