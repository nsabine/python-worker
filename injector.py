#!/usr/bin/env python

import time
import redis
import os

print("Staring injector")

host="redis"
password=os.environ['REDIS_PASSWORD']

r = redis.Redis(name="job", host=host, password=password)
print("Injector with sessionID: " +  r.sessionID())
for x in range(100):
  r.rpush("job", r.sessionID + " " + x)
print("Injector complete, exiting")
