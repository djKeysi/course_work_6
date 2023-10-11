from django import forms

from mailing.models import ClientServices


class ClientServicesForm(forms.ModelForm):
    class Meta:
        model = ClientServices
        fields = '__all__'
