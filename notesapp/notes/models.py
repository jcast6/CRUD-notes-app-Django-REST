# Import necessary modules and classes
from django.db import models

# Define the Note model class, which inherits from models.Model
class Note(models.Model):
    # Define fields for the Note model
    # The title field is a CharField with a maximum length of 255 characters
    # can be null and/or blank when creating a new note for the first time
    title = models.CharField(max_length=255, null=True, blank=True)
    # The content field is a TextField
    # It can be null and/or blank when creating a new note for the first time
    content = models.TextField(null=True, blank=True)

    # The last_updated_on field is a DateTimeField that is automatically updated each time a Note object is saved
    last_updated_on = models.DateTimeField(auto_now=True)

    # The is_active field is a BooleanField that defaults to True
    # To delete a Note object, we will simply set is_active to False
    is_active = models.BooleanField(default=True)

    # method to return the title of the Note object as a string
    def __str__(self):
        return self.title
