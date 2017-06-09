#!/usr/bin/env python

import time
import redis
import os
import sys

print("Starting injector")
sys.stdout.flush()

host="redis"
password=os.environ['REDIS_PASSWORD']

r = redis.Redis(host=host, password=password)
for x in range(100):
  print("Injecting Job: " + x)
  sys.stdout.flush()
  r.rpush("job", x)
print("Injector complete, exiting")
sys.stdout.flush()
