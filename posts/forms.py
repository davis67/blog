from django import forms
from . import models


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ("title", "photo", "description", "category")


class AddReplyForm(forms.Form):
    description = forms.CharField()

    def clean(self):
        description = self.cleaned_data.get("description")
        return self.cleaned_data


class AddCommentForm(forms.Form):
    description = forms.CharField()

    def clean(self):
        description = self.cleaned_data.get("description")
        return self.cleaned_data
