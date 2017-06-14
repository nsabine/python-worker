#!/usr/bin/env python

import time
import rediswq
import os
import sys
import socket

print("Starting worker")
sys.stdout.flush()

host="redis"
ip=socket.gethostbyname(host)
password=os.environ['REDIS_PASSWORD']

# Uncomment next two lines if you do not have Kube-DNS working.
# import os
# host = os.getenv("REDIS_SERVICE_HOST")
print("About to connect to Redis at host: " + host + ", and ip: " + ip)
sys.stdout.flush()

# q = rediswq.RedisWQ(name="job", host=host, password=password, socket_connect_timeout=10)
q = rediswq.RedisWQ(name="job", host=host, socket_connect_timeout=10)
print("Worker with sessionID: " +  q.sessionID())
print("Initial queue state: empty=" + str(q.empty()))
sys.stdout.flush()

while not q.empty():
  item = q.lease(lease_secs=10, block=True, timeout=2)
  if item is not None:
    itemstr = item.decode("utf=8")
    print("Working on " + itemstr)
    sys.stdout.flush()
    time.sleep(10) # Put your actual work here instead of sleep.
    q.complete(item)
  else:
    print("Waiting for work")
    sys.stdout.flush()
print("Queue empty, exiting")
sys.stdout.flush()
