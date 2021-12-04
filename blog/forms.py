from django import forms
from .models import BlogPost


class NewBlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['topic', 'text', 'public']
        labels = {
            'topic': '题目',
            'text': '文字',
            'public': '是否公开'
        }
