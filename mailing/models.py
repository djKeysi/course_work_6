from django.db import models


NULLABLE = {'blank': True, 'null': True}
class ClientServices(models.Model):
    email = models.EmailField(max_length=50, verbose_name='контактный email')
    surname = models.CharField(max_length=50, verbose_name='фамилия')
    name = models.CharField(max_length=50, verbose_name='имя')
    last_name = models.CharField(max_length=50, verbose_name='отчество')
    comment = models.TextField(max_length=200, verbose_name='комментарий')

    def __str__(self):
        return f'{self.name}{self.surname}{self.last_name}'
    class Meta:
        verbose_name = 'Клиент сервиса'
        verbose_name_plural = 'Клиенты сервисов'

class MailingSetting(models.Model):
    time_mailing= models.DateTimeField(auto_now_add=True, blank=True, verbose_name='время рассылки')

    client = models.ManyToManyField(ClientServices)
    #должны менятся автоматически чоисес необязателен
    STATUS_MAILING = (
        ('created', 'создана'),
        ('launched', 'запущена'),
        ('completed', 'завершена'),
    )
    status_mailing = models.CharField(max_length=1, choices=STATUS_MAILING,verbose_name='статус рассылки')

    # PEREODICITY = (
    #     ('one_day', 'раз в день'),
    #     ('one_week', 'раз в неделю'),
    #     ('one_month', 'раз в месяц'),
    # )
    # periodicity  = models.CharField(max_length=1, choices=PEREODICITY,verbose_name='переодичность')
    class Period(models.TextChoices):
        DAILY = 'раз в день'
        MONTHLY = 'раз в месяц'
        WEEKLY = 'раз в неделю'

    periodicity = models.CharField(max_length=1,choices=Period.choices,default=Period.DAILY,verbose_name='переодичность')

    def __str__(self):
        return f'{self.status_mailing}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

class Message(models.Model):
    mailing_setting = models.ForeignKey(MailingSetting, on_delete = models.CASCADE)
    letter_message =  models.CharField(max_length=100, verbose_name='тема письма')
    body_message =  models.TextField(max_length=200, verbose_name='тело письма')

    def __str__(self):
        return f'{self.mailing_setting}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

class LogMailing(models.Model):
    mailing_settings = models.ForeignKey(MailingSetting, on_delete=models.CASCADE)
    status = models.CharField(max_length=150, verbose_name='статус попытки')
    otvet = models.CharField(max_length=150, verbose_name='ответ почтового сервера, если он был.')
    #дата и время последней попытки

    def __str__(self):
        return f'{self.mailing_settings}'

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'





