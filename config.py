from multiprocessing import cpu_count

workers = cpu_count()
worker_class = 'sync'
bind = '0.0.0.0:8000'