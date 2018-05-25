from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from reminder.forms import ReminderForm
from reminder.models import Reminder


class ReminderList(ListView):
    model = Reminder
    template_name = 'index.html'


class ReminderDetail(DetailView):
    model = Reminder
    template_name = 'detail.html'


class ReminderCreate(CreateView):
    model = Reminder
    form_class = ReminderForm
    template_name = 'create.html'


class ReminderUpdate(UpdateView):
    model = Reminder
    form_class = ReminderForm
    template_name = 'create.html'


class ReminderDelete(DeleteView):
    model = Reminder
    template_name = 'delete.html'

    def get_success_url(self):
        return reverse('index')
