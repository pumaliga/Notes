from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from app.API.serializers import RegisterSerializer, NoteSerializer
from app.models import Note


class NoteList(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

