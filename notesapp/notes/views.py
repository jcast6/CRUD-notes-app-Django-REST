# Import necessary modules and classes
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.viewsets import ModelViewSet
from .models import Note
from .serializers import NoteSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import action

# Define the NoteViewSet class, which inherits from ModelViewSet
class NoteViewSet(ModelViewSet):
    # Set the serializer and renderer classes for this view
    serializer_class = NoteSerializer
    renderer_classes = [TemplateHTMLRenderer]

    # Define a method to get a Note object based on its primary key (id)
    def get_object(self, pk=None):
        # If no pk is passed, get it from the request query parameters
        if pk is None:
            pk = self.request.query_params.get("id")
        # Use the get_object_or_404 shortcut to get the Note object
        return get_object_or_404(Note, id=pk)

    # Define a method to get the queryset of Note objects to display
    def get_queryset(self):
        # Filter by active notes and order by last_updated_on in descending order
        return Note.objects.filter(is_active=True).order_by('-last_updated_on')

    # Define a method to perform a "soft delete" on a Note object
    def perform_destroy(self, instance):
        # Set the is_active field to False and save the instance
        instance.is_active = False
        instance.save()

    # Define a method to handle the GET and POST requests for the note list page
    def list(self, request):
        # Get the queryset of Note objects
        queryset = self.get_queryset()
        # If the request method is POST, create a new note and redirect to the note list page
        if request.method == 'POST':
            new_note = Note(title=request.POST['title'], content=request.POST['content'])
            new_note.save()
            return redirect('note-list')
        # If the request method is GET, render the note list template with the queryset
        return render(request, 'note_list.html', {'notes': queryset})

    # Define an action method to handle the POST request for updating a Note object
    @action(detail=True, methods=['post'])
    @csrf_exempt
    def update(self, request, pk=None):
        # Get the Note object to update
        note = self.get_object(pk=pk)
        # Update the title and content fields with the POST data
        note.title = request.POST['title']
        note.content = request.POST['content']
        note.save()
        # Redirect to the note list page
        return redirect('note-list')

    # Define an action method to handle the POST request for deleting a Note object
    @action(detail=True, methods=['post'])
    @csrf_exempt
    def delete(self, request, pk=None):
        # Get the Note object to delete
        note = self.get_object(pk=pk)
        # Delete the Note object
        note.delete()
        # Redirect to the note list page
        return redirect('note-list')
