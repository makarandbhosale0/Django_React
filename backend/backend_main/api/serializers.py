from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Notes

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {"password": {"write_only": True}}  #tells django that we want to accept password but dont want to return it 


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['id', 'title', 'content', 'created_at', 'author']
        extra_kwargs = {"author": {"read_only": True}}  #to read only who the author is and not to accept it when creating a note, we will set it in the view based on the logged in user

