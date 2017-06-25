import os



REDIS_HOST =  os.environ['REDIS_SERVICE_HOST']
REDIS_PORT =  os.environ['REDIS_SERVICE_PORT']
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']

QUEUES = ['default']
#REDIS_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'

forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }
