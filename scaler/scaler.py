import requests                                                                                                                                                                                                                        
import os                                                                                                                                                                                                                              
import sys

print("Starting scaler")
sys.stdout.flush()

                                                                                                                                                                                                                                       
host=os.environ['KUBERNETES_SERVICE_HOST']                                                                                                                                                                                             
tokenfile = open('/var/run/secrets/kubernetes.io/serviceaccount/token','r')                                                                                                                                                            
token=tokenfile.read()                                                                                                                                                                                                                      
url = 'https://' + host + ':8443/oapi/v1'                                                                                                                                                                                              

print("host: " + host)
print("url: " + url)
print("token: " + token)
sys.stdout.flush()
                                                                                                                                                                                                                                       
headers = {'Authorization': 'Bearer ' + token}                                                                                                                                                                                         
print(requests.get(url, headers=headers, verify=False))
sys.stdout.flush()
