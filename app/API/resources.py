from rest_framework import permissions, viewsets, mixins

from app.API.serializers import NoteSerializer
from app.models import Note


class NoteList(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


