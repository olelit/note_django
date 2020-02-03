from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth import authenticate, login
import json
from notify.forms import NoteForm, AuthForm, SortNote
from notify.models import Note
from django.http import JsonResponse


def get_note(request):
    params = json.loads(request.body.decode('utf-8'))
    note = Note.objects.get(pk=params['id'])
    json_data = json.dumps(note.body)
    return HttpResponse(json_data, content_type="application/json")


class NotifyListView(ListView):
    template_name = 'index.html'
    paginate_by = 15
    model = Note

    def get_queryset(self, **kwargs):
        sort = self.request.GET.get('ordering')
        default_sort = '-created_at'
        if sort is not None:
            default_sort = sort
        return Note.objects.filter(author=self.request.user.id).order_by(default_sort)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_form'] = NoteForm()
        context['auth_form'] = AuthForm()
        context['sort'] = SortNote()
        return context
