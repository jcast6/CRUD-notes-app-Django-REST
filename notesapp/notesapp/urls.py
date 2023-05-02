"""notesapp URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from notes.views import NoteViewSet

# urlpatterns is a list that stores the URL patterns for the application
urlpatterns = [
    # The first URL pattern maps the 'notes/' path to the NoteViewSet class.
    # For GET request, the 'list' method will be called. For POST request, the 'list' method will also be called.
    # The name 'note-list' is given to this URL pattern for easier reference in other parts of the application.
    path('notes/', NoteViewSet.as_view({'get': 'list', 'post': 'list'}), name='note-list'),

    # The second URL pattern maps the 'notes/<int:pk>/update/' path to the NoteViewSet class.
    # This path includes a parameter 'pk', which is an integer representing the primary key (id) of a Note object.
    # For POST request, the 'update' method will be called.
    # The name 'note-update' is given to this URL pattern for easier reference in other parts of the application.
    path('notes/<int:pk>/update/', NoteViewSet.as_view({'post': 'update'}), name='note-update'),

    # The third URL pattern maps the 'notes/<int:pk>/delete/' path to the NoteViewSet class.
    # This path also includes a parameter 'pk', which is an integer representing the primary key (id) of a Note object.
    # For POST request, the 'delete' method will be called.
    # The name 'note-delete' is given to this URL pattern for easier reference in other parts of the application.
    path('notes/<int:pk>/delete/', NoteViewSet.as_view({'post': 'delete'}), name='note-delete'),
]

