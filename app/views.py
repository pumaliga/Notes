from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, TemplateView

from app.forms import RegisterForm, UpdateNoteForm
from app.models import Note


class Login(LoginView):
    success_url = '/'
    template_name = 'login.html'


class Register(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = '/'


class Logout(LoginRequiredMixin, LogoutView):
    next_page = '/'
    login_url = 'login/'


class NoteListView(LoginRequiredMixin, ListView):
    login_url = 'login/'
    model = Note
    template_name = 'index.html'
    paginate_by = 6


class CreateNote(CreateView):
    model = Note
    fields = ['title', 'text']
    template_name = 'create_note.html'
    success_url = '/'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form=form)


class NoteUpdate(UpdateView):
    model = Note
    form_class = UpdateNoteForm
    template_name = 'update_note.html'
    success_url = '/'


class NoteDelete(DeleteView):
    model = Note
    success_url = '/'


class AboutView(TemplateView):
    template_name = 'about.html'
