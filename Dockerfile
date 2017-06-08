FROM registry.access.redhat.com/rhscl/python-34-rhel7

RUN LD_LIBRARY_PATH=/opt/rh/rh-python34/root/usr/lib64:/opt/rh/httpd24/root/usr/lib64 pip install redis
COPY ./worker.py /worker.py
COPY ./rediswq.py /rediswq.py

CMD  python worker.py
