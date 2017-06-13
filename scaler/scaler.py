import requests                                                                                                                                                                                                                        
import os                                                                                                                                                                                                                              
import sys

print("Starting scaler")
sys.stdout.flush()

                                                                                                                                                                                                                                       
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
print(r.text)
sys.stdout.flush()
