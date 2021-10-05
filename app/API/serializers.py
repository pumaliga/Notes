from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers
from app.models import Note


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def save(self, **kwargs):
        self.validated_data["password"] = make_password(self.validated_data["password"])
        return super().save()


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['title', 'text']




