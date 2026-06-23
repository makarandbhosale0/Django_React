from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import NotesSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Notes

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  #tells who can access this 

class CreateNote(generics.ListCreateAPIView):
    serializer_class = NotesSerializer
    permission_classes = [IsAuthenticated]  #only authenticated users can create and view notes

    def get_queryset(self):
        user = self.request.user
        return Notes.objects.filter(author=user)  #only return notes created by the logged in user
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)  #set the author of the note to the logged in user
        else:
            print(serializer.errors)

class DeleteNote(generics.DestroyAPIView):
    serializer_class = NotesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Notes.objects.filter(author=user)  #only allow users to delete their own notes