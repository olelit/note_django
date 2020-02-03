from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Note


def save(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect(request.POST['destination'])


def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
    return HttpResponseRedirect(request.POST['destination'])


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('name', 'body', 'author')


class AuthForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class SortNote(forms.Form):
    ordering = forms.ChoiceField(label='Сортировка', required=False, choices=[
        ['name', 'По названию начиная с начала'],
        ['-name', 'По названию начиная с конца'],
        ['created_at', 'Начиная с ранних'],
        ['-created_at', 'Начиная с последних']
    ])