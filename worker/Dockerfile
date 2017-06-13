FROM registry.access.redhat.com/rhscl/python-34-rhel7

# RUN LD_LIBRARY_PATH=/opt/rh/rh-python34/root/usr/lib64:/opt/rh/httpd24/root/usr/lib64 pip install redis
COPY ./requirements.txt /opt/app-root/src/requirements.txt
RUN LD_LIBRARY_PATH=/opt/rh/rh-python34/root/usr/lib64:/opt/rh/httpd24/root/usr/lib64 pip install -r requirements.txt
COPY ./rediswq.py /opt/app-root/src/rediswq.py
COPY ./worker.py /opt/app-root/src/worker.py

CMD  python worker.py
