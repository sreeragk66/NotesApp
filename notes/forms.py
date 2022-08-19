from notes.models import Note
from django import forms
from django.forms import ModelForm

class NoteCreationForm(ModelForm):
    class Meta:
        model=Note
        fields=[
            "title","content","image"
        ]

        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "content":forms.Textarea(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"})
        }