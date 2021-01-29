from django.forms import ModelForm
from django import forms
from projects.models import Project,Comment

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name','description']
        widgets = { 'description' : forms.Textarea()} 

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = { 'text' : forms.Textarea()} 