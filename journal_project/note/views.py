from rest_framework import generics
from .models import NoteModel
from .serializers import NoteSerializer
from .permissions import IsAuthorOrReadOnly


class NoteListView(generics.ListCreateAPIView):
    queryset = NoteModel.objects.all()
    serializer_class = NoteSerializer

class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = NoteModel.objects.all()
    serializer_class = NoteSerializer
    
