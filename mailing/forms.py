from django import forms

from mailing.models import ClientServices, MailingSetting, Message


class ClientServicesForm(forms.ModelForm):

    class Meta:
        model = ClientServices
        fields = '__all__'





class MailingSettingForm(forms.ModelForm):

    class Meta:
        model = MailingSetting
        fields = '__all__'
        widgets = {
            'client': forms.CheckboxSelectMultiple,
            #'time_mailing': forms.DateInput(attrs={'class': 'datepicker'}),
        }

    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop('user', None)
    #     super(MailingSettingForm, self).__init__(*args, **kwargs)
    #     self.fields['client'].queryset = user.client_set.all()

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

