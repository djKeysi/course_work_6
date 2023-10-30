from django.db import models


NULLABLE = {'blank': True, 'null': True}
class ClientServices(models.Model):

    # surname = models.CharField(max_length=50, verbose_name='фамилия')
    # name = models.CharField(max_length=50, verbose_name='имя')
    # last_name = models.CharField(max_length=50, verbose_name='отчество')
    full_name = models.CharField(max_length=50,blank=True, verbose_name='ФИО')
    email = models.EmailField(max_length=50,blank=True, verbose_name='контактный email')
    comment = models.TextField(max_length=200, **NULLABLE, verbose_name='комментарий')

    def __str__(self):
        return f'{self.full_name}'
    class Meta:
        verbose_name = 'Клиент сервиса'
        verbose_name_plural = 'Клиенты сервисов'

class MailingSetting(models.Model):
    client = models.ManyToManyField(ClientServices,verbose_name='клиенты')
    #должны менятся автоматически чоисес необязателен
    STATUS_MAILING = (
        ('создана','создана'),
        ('запущена','запущена'),
        ('завершена','завершена'),
    )
    status_mailing = models.CharField(max_length=10, choices=STATUS_MAILING,verbose_name='статус рассылки')

        # время начало и конец
    time_mailing= models.DateTimeField(verbose_name='время рассылки')

    PERIOD=(
        ('раз в день', 'раз в день'),
        ('раз в месяц', 'раз в месяц'),
        ('раз в неделю', 'раз в неделю'),
        # DAILY = 'раз в день'
        # MONTHLY = 'раз в месяц'
        # WEEKLY = 'раз в неделю'
    )

    periodicity = models.CharField(max_length=15,choices=PERIOD,verbose_name='переодичность')

    def __str__(self):
        return f'{self.client}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

class Message(models.Model):
    mailing_setting = models.ForeignKey(MailingSetting, on_delete = models.CASCADE, verbose_name='Рассылка')
    letter_message =  models.CharField(max_length=100, verbose_name='тема письма')
    body_message =  models.TextField(max_length=200, verbose_name='тело письма')

    def __str__(self):
        return f'{self.mailing_setting.time_mailing}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

class LogMailing(models.Model):
    mailing_settings = models.ForeignKey(MailingSetting, on_delete=models.CASCADE)
    client = models.ForeignKey(ClientServices, on_delete=models.CASCADE)
    STATUS_LOG = (
        ('OK', 'OK'),
        ('Fail', 'Fail'),
    )
    status = models.CharField(max_length=150,choices=STATUS_LOG, verbose_name='статус попытки')
    response_mail_server = models.CharField(max_length=150, verbose_name='ответ почтового сервера')

    attempts = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='дата и время последней попытки')

    def __str__(self):
        return f'{self.mailing_settings}'

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'





