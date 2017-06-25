import os
import redis
#from redis import StrictRedis
from rq import Connection, Queue
import work

# use the kubernetes service environment variables to
#  connect to the redis queue

REDIS_HOST =  os.environ['REDIS_SERVICE_HOST']
REDIS_PORT =  os.environ['REDIS_SERVICE_PORT']
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']

#REDIS_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
QUEUES = ['default']

#connection=StrictRedis(host=REDIS_HOST, port=REDIS_PORT)

def add_jobs():
  #redis_connection = redis.from_url(REDIS_URL)
  redis_connection = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)
  q = Queue(connection=redis_connection)
  for i in range(1,100):
    job = q.enqueue(do_work, result_ttl=60000)

if __name__ == '__main__':
  add_jobs()
