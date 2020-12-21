import multiprocessing


bind = "127.0.0.1:9090"
# workers = multiprocessing.cpu_count()
timeout = 36000
workers = 1
max_requests = 1000
max_requests_jitter = 50
worker_class = 'aiohttp.GunicornUVLoopWebWorker'
