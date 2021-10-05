from django.urls import path
from app.views import Login, Register, Logout, NoteListView, CreateNote, NoteUpdate, NoteDelete, AboutView


urlpatterns = [
    path('', NoteListView.as_view(), name='base'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', Logout.as_view(), name='logout'),
    path('new-note/', CreateNote.as_view(), name='new_note'),
    path('note-update/<int:pk>/', NoteUpdate.as_view(), name='note_update'),
    path('note-delete/<int:pk>/', NoteDelete.as_view(), name='note_delete'),
    path('about/', AboutView.as_view(), name='about'),

]

