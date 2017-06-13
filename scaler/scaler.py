import os                                                                                                                                                                                                                              
import sys
from pprint import pprint

from __future__ import print_function

print("Starting scaler")
sys.stdout.flush()

                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                       
namespace=os.environ['NAMESPACE']                                                                                                                                                                                             
host=os.environ['KUBERNETES_SERVICE_HOST']                                                                                                                                                                                             
port=os.environ['KUBERNETES_SERVICE_PORT']                                                                                                                                                                                             
tokenfile = open('/var/run/secrets/kubernetes.io/serviceaccount/token','r')                                                                                                                                                            
token=tokenfile.read()                                                                                                                                                                                                                      
url = 'https://' + host + ':' + port + '/oapi/v1'                                                                                                                                                                                              

print("host: " + host)
print("port: " + port)
print("url: " + url)
print("token: " + token)
sys.stdout.flush()
                                                                                                                                                                                                                                       
headers = {'Authorization': 'Bearer ' + token}                                                                                                                                                                                         
r = requests.get(url, headers=headers, verify=False)
pprint(r.text)
sys.stdout.flush()


url = 'https://' + host + ':' + port + '/oapi/v1/namespaces/' + namespace + '/deploymentconfigs/python-scaler'
headers = {'Authorization': 'Bearer ' + token}                                                                                                                                                                                         
patch = 'spec: \n  replicas: 2'
r = requests.patch(url, headers=headers, json=patch, verify=False)
pprint(r.text)
sys.stdout.flush()

