from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from app.models import Note


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']


class UpdateNoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text']



