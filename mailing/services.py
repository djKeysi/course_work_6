import datetime

from django.conf import settings
from django.core.mail import send_mail

from mailing.models import MailingSetting, LogMailing

from apscheduler.schedulers.background import BackgroundScheduler



def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_mailings, 'interval', seconds=15)
    scheduler.start()  #как вызвать в проекте ?

def send_mailings():
    current_datetime = datetime.now()
    for mailing in MailingSetting.objects.filter(status_mailing='создана'):
        is_mailing = False
        emails = [client.email for client in mailing.client.all()]
        month_start = mailing.start_time.month
        day_start = mailing.start_time.day
        hour_start = mailing.start_time.hour
        minut_start = mailing.start_time.minute
        attempt_status = 'Успешно'
        server_response = 'Сообщение доставлено'
        messages = mailing.message_set.all()

        if mailing.time_mailing == 'раз в день' and day_start == current_datetime.day \
                and current_datetime.hour == hour_start and current_datetime.minute == minut_start:
            mailing.start_time = mailing.start_time + datetime.timedelta(days=1)
            is_mailing = True

        elif mailing.time_mailing == 'раз в месяц' and day_start == current_datetime.day \
                and current_datetime.hour == hour_start and current_datetime.minute == minut_start:
            mailing.start_time = mailing.start_time + datetime.timedelta(days=7)
            is_mailing = True

        elif mailing.time_mailing == 'раз в неделю' and month_start == current_datetime.month \
                and day_start == current_datetime.day \
                and current_datetime.hour == hour_start and current_datetime.minute == minut_start:
            mailing.start_time = mailing.start_time + datetime.timedelta(days=30)
            is_mailing = True

        if is_mailing:
            mailing.save()
            for message in messages:
                try:

                    send_mail(
                        subject=message.subject,
                        message=message.body,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=emails
                    )

                except Exception as e:

                    attempt_status = 'error'
                    server_response = str(e)

                finally:

                    LogMailing.objects.create(status=message,
                                       attempts=attempt_status,
                                       response_mail_server=server_response)
