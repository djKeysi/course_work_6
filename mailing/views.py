from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView, DeleteView

from mailing.forms import ClientServicesForm, MailingSettingForm
from mailing.models import ClientServices, MailingSetting


class IndexView(TemplateView):
    template_name = 'mailing/index.html'
    #context_object_name = 'clients'
    # r = ClientServices.objects.all()
    #
    # extra_context = {
    #     'title': 'Главная страница11',
    #     'clients': r
    #
    # }

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     clientservices = ClientServices.objects.all()
    #     context_data['products'] = clientservices
    #     return context_data


class ClientServicesCreateView(CreateView):
    model = ClientServices
    form_class = ClientServicesForm
    success_url = reverse_lazy('mailing:index')
# class MailingSettingCreateView(CreateView):
#     model = MailingSetting
#     form_class = MailingSettingForm
#     success_url = reverse_lazy('mailing:index')

class ClientServicesListView(ListView):
    model = ClientServices

    template_name = 'mailing/update_delete_clients.html'

    r = ClientServices.objects.all()

    extra_context = {
       'clients': r

    }


class ClientServicesUpdateView(UpdateView):
    model = ClientServices
    form_class = ClientServicesForm
    success_url = reverse_lazy('mailing:update_client')


class ClientServicesDeleteView(DeleteView):
    model = ClientServices
    form_class = ClientServicesForm
    success_url = reverse_lazy('mailing:update_client')



    #success_url = reverse_lazy('mailing:index')

