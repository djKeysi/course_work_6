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
    path('delete_clients/', views.ClientServicesListView.as_view(), name='client_delete'),




   # path('mailingsetting/', MailingSettingCreateView.as_view(), name='maililngsetting_create'),
]