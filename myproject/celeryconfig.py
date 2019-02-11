### Broker settings.
broker_host = 'cache'
broker_port = '6379'
broker_url = 'redis://%s:%s/0' % (broker_host, broker_port)

# imports = ('myproject.task',)

result_backend = 'django-cache'

### configuration worker
worker_concurrency = 4

# for debug
worker_max_tasks_per_child = 10

### logging
worker_log_format = "[%(asctime)s: %(levelname)s/%(processName)s] %(message)s"

worker_task_log_format = """[%(asctime)s: %(levelname)s/%(processName)s]
                            [%(task_name)s(%(task_id)s)] %(message)s"""
