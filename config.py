import os
from multiprocessing import cpu_count

ENV = os.getenv("ENV")
workers = cpu_count() if ENV != 'local' else 1
worker_class = 'sync'
bind = '0.0.0.0:8000'
