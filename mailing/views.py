from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView, DeleteView

from mailing.forms import ClientServicesForm, MailingSettingForm, MessageForm
from mailing.models import ClientServices, MailingSetting, Message


class IndexView(TemplateView):
    template_name = 'mailing/index.html'
    #context_object_name = 'clients'
    # r = ClientServices.objects.all()
    #
    extra_context = {
         'title': 'Главная страница',
     }

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     clientservices = ClientServices.objects.all()
    #     context_data['products'] = clientservices
    #     return context_data


class ClientServicesCreateView(CreateView):
    model = ClientServices
    form_class = ClientServicesForm
    success_url = reverse_lazy('mailing:index')
class ClientServicesListView(ListView):
    model = ClientServices
    template_name = 'mailing/update_delete_clients.html'

    clients = ClientServices.objects.all()

    extra_context = {
       'clients': clients,
    }


class ClientServicesUpdateView(UpdateView):
    model = ClientServices
    form_class = ClientServicesForm
    success_url = reverse_lazy('mailing:index')

class ClientServicesDeleteView(DeleteView):
    model = ClientServices
    form_class = ClientServicesForm
    success_url = reverse_lazy('mailing:index')

class MailingSettingCreateView(CreateView):
    model = MailingSetting
    form_class = MailingSettingForm
    success_url = reverse_lazy('mailing:index')

class MailingSettingListView(ListView):
    model = MailingSetting
    template_name = 'mailing/update_delete_mailing.html'
    mailing = MailingSetting.objects.all()

    extra_context = {
            'mailing': mailing,
        }
class MailingSettingUpdateView(UpdateView):
    model = MailingSetting
    form_class = MailingSettingForm
    success_url = reverse_lazy('mailing:index')

class MailingSettingDeleteView(DeleteView):
    model = MailingSetting
    form_class = MailingSettingForm
    success_url = reverse_lazy('mailing:index')


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:index')


