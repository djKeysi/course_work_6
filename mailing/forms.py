from django import forms

from mailing.models import ClientServices, MailingSetting


class ClientServicesForm(forms.ModelForm):
    class Meta:
        model = ClientServices
        fields = '__all__'


class MailingSettingForm(forms.ModelForm):
    class Meta:
        model = MailingSetting
        exclude = '__all__'
