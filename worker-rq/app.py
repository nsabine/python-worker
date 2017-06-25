import os
import redis
#from redis import StrictRedis
from rq import Connection, Worker

# use the kubernetes service environment variables to
#  connect to the redis queue

REDIS_HOST =  os.environ['REDIS_SERVICE_HOST']
REDIS_PORT =  os.environ['REDIS_SERVICE_PORT']
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']

#REDIS_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
QUEUES = ['default']

#connection=StrictRedis(host=REDIS_HOST, port=REDIS_PORT)

def runworker():
  #redis_connection = redis.from_url(REDIS_URL)
  redis_connection = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)
  with Connection(redis_connection):
    worker = Worker(QUEUES)
    worker.work()

if __name__ == '__main__':
  runworker()
