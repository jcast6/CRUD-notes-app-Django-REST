# Import necessary modules and classes
from rest_framework import serializers
from .models import Note

# Define the NoteSerializer class, which inherits from ModelSerializer
class NoteSerializer(serializers.ModelSerializer):
    # Define a read-only field for is_active
    is_active = serializers.BooleanField(read_only=True)

    # Define the Meta class to specify the model and fields to serialize
    class Meta:
        model = Note
        fields = ('id', 'title', 'content', 'last_updated_on', 'is_active')
