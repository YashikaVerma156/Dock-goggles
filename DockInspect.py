#from __future__ import division
import requests_unixsocket
import json
import os

#def logs(c_id):
 #   base = "http+unix://%2Fvar%2Frun%2Fdocker.sock"
 #  url = "/events"
#   session = requests_unixsocket.Session()
#   resp=session.get(base + url, stream= True)
#   print(resp.iter_lines())

def logs(c_id):
    base = "http+unix://%2Fvar%2Frun%2Fdocker.sock"
    url = "/events"
    session = requests_unixsocket.Session()
    resp=session.get(base + url, stream= True)
    #for res in resp.json():
        #a='{}'.format(res["memory_stats"])
    #print(resp.content)
    print(resp.content)

def proc(c_id,stream):
    base = "http+unix://%2Fvar%2Frun%2Fdocker.sock"
    url = "/containers/%s/top?ps_args=%s" % (c_id,stream)
    session = requests_unixsocket.Session()
    resp=session.get(base+url)
    #for res in resp.json():
        #a='{}'.format(res["memory_stats"])
    #print(resp.content)
    a=resp.json()
    print("%s" % a["Titles"])
    print(a["Processes"]) 

def ins(c_id,stream):
    base = "http+unix://%2Fvar%2Frun%2Fdocker.sock"
    url = "/containers/%s/stats?stream=%s" % (c_id,stream)
    session = requests_unixsocket.Session()
    resp=session.get(base+url)
    #for res in resp.json():
        #a='{}'.format(res["memory_stats"])
    #print(resp.content)
    a=resp.json()
    b=a["memory_stats"]["usage"]
    c=a["memory_stats"]["max_usage"]
    print("At date & time : %s "% a["read"])
    print("Memory usage : %s"% ((float(b)*100)/float(c)))
    #b=a[cpu_stats][][]
    print("CPU_usage in naoseconds : %s"% a["cpu_stats"]["cpu_usage"]["total_usage"])

base = "http+unix://%2Fvar%2Frun%2Fdocker.sock"
url = "/containers/json"
session = requests_unixsocket.Session()
resp=session.get(base+url)      
print("No. of containers running are : %s " % sum(1 for i in resp.json()))
for item in resp.json():
    #print(resp.content)
    print(" ")
    a=item["Id"]
    print("processId :")
    os.system("sudo docker inspect -f '{{.State.Pid}}' " + a)
    print("Container Id : %s" % item["Id"])
    print("Container name : %s" % item["Names"][0])
    print("Container status : %s" % item["Status"])
    print("Container state : %s" % item["State"])
    print("Container Image Name : %s " % item["Image"])
    print("Container Image ID : %s" % item["ImageID"])
    print("Command inside the container : %s" % item["Command"])
    print("Container NetworkID : %s" % item["NetworkSettings"]["Networks"]["bridge"]["NetworkID"])
    print("Container MacAddress : %s" % item["NetworkSettings"]["Networks"]["bridge"]["MacAddress"])
    print("Container Gateway : %s" % item["NetworkSettings"]["Networks"]["bridge"]["Gateway"])
    print("Container IP Address : %s" % item["NetworkSettings"]["Networks"]["bridge"]["IPAddress"])
    ins(a, 0)
    #logs(a)
    proc(a, "ef")
