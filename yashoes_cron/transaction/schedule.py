from myproject import task_app


task_app.conf.beat_schedule = {
    'every-30-seconds': {
        'task': 'yashoes_cron.transaction.task.test',
        'schedule': 30,
    }
}
