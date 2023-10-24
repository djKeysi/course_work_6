from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView

from mailing.forms import ClientServicesForm, MailingSettingForm
from mailing.models import ClientServices, MailingSetting


class IndexView(TemplateView):
    template_name = 'mailing/index.html'
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

class MailingSettingUpdateView(UpdateView):
    model = MailingSetting
    form_class = MailingSettingForm
    context_object_name = 'posts'

    #success_url = reverse_lazy('mailing:index')

