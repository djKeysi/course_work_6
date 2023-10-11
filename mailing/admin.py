from django.contrib import admin

from mailing.models import ClientServices, MailingSetting, Message, LogMailing


@admin.register(ClientServices)
class ClientServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'last_name', 'comment')


@admin.register(MailingSetting)
class MailingSettingAdmin(admin.ModelAdmin):
    list_display = ('time_mailing', 'status_mailing', 'periodicity')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('mailing_setting', 'letter_message', 'body_message')
    #list_display_links = ('id', 'client')


@admin.register(LogMailing)
class LogMailingAdmin(admin.ModelAdmin):
    list_display = ('mailing_settings', 'status', 'otvet', 'attempts')
