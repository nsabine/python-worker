#!/bin/bash

export LC_ALL=en_US.utf8
export LANG=en_US.utf8

rq-dashboard --port 8080 --redis-host $DATABASE_SERVICE_NAME --redis-port 6379 --redis-password $REDIS_PASSWORD
