from django.urls import path

from mailing.apps import MailingConfig
from . import views

app_name=MailingConfig.name





urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('сreate/', views.ClientServicesCreateView.as_view(), name='client_create'),
    path('update/<int:pk>/', views.ClientServicesUpdateView.as_view(), name='client_update'),
    path('update_delete_clients/', views.ClientServicesListView.as_view(), name='update_delete_clients'),
    path('delete/<int:pk>/', views.ClientServicesDeleteView.as_view(), name='delete_client'),


    path('сreate_mailing/', views.MailingSettingCreateView.as_view(), name='create_mailing'),
    path('update_delete_mailing/', views.MailingSettingListView.as_view(), name='update_delete_mailing'),
    path('update_mailing/<int:pk>/', views.MailingSettingUpdateView.as_view(), name='update_mailing'),
    path('delete_mailing/<int:pk>/', views.MailingSettingDeleteView.as_view(), name='delete_mailing'),


    path('сreate_message/', views.MessageCreateView.as_view(), name='create_message'),
    path('update_delete_message/', views.MessageListView.as_view(), name='update_delete_message'),
    path('update_message/<int:pk>/', views.MessageUpdateView.as_view(), name='update_message'),
    path('delete_message/<int:pk>/', views.MessageDeleteView.as_view(), name='delete_message'),

    path('logs/', views.LogListView.as_view(), name='logs'),












   # path('mailingsetting/', MailingSettingCreateView.as_view(), name='maililngsetting_create'),
]