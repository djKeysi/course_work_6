
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


def job():
    print('Hello APScheduler')


scheduler = BlockingScheduler()
#раз в день в 19-59
scheduler.add_job(job, 'cron', day_of_week='0-6', hour=19, minute=59)
#раз в месяц в понедельник в 19-59
scheduler.add_job(job, 'cron', month='1-12', day_of_week='0', hour=19, minute=59)
#раз в год в понедельник в 19-59
scheduler.add_job(job, 'cron', year='2023', day_of_week='0', hour=19, minute=59)

scheduler.start()