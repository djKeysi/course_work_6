from django.urls import path

from mailing.apps import MailingConfig
from . import views

app_name=MailingConfig.name





urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('сreate/', views.ClientServicesCreateView.as_view(), name='client_create'),
    path('update/<int:pk>/', views.MailingSettingUpdateView.as_view(), name='client_update'),



   # path('mailingsetting/', MailingSettingCreateView.as_view(), name='maililngsetting_create'),
]