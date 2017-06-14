#!/usr/bin/env python

import time
import redis
import os
import sys

print("Starting injector")
sys.stdout.flush()

host="redis"
password=os.environ['REDIS_PASSWORD']

r = redis.Redis(host=host, password=password, connect_timeout=5)
for x in range(100):
  print("Injecting Job: " + str(x))
  sys.stdout.flush()
  r.rpush("job", str(x))
print("Injector complete, exiting")
sys.stdout.flush()
