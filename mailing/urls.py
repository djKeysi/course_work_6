from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import IndexView, ClientServicesCreateView, ClientServicesUpdateView, MailingSettingCreateView

app_name=MailingConfig.name





urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('сreate/', ClientServicesCreateView.as_view(), name='client_create'),
    path('update/<int:pk>/', ClientServicesUpdateView.as_view(), name='client_update'),

    path('mailingsetting/', MailingSettingCreateView.as_view(), name='maililngsetting_create'),
]