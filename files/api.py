#!/usr/bin/python3

from klein import Klein, run, route
import re
import json

app = Klein()

@app.route('/api/MemFree')
def getfreemem(request):
    with open('/proc/meminfo', 'r') as f:
        freemem = f.readlines()[1]
        MemFree=re.findall(r'\d+ kB', freemem)[0]
        return json.dumps({"MemFree":MemFree})

@app.route('/api/SReclaimable')
def getrecmem(request):
    with open('/proc/meminfo', 'r') as f:
        meminfo = f.readlines()[22]
        SReclaimable=re.findall(r'\d+ kB', meminfo)[0]
        return json.dumps({"SReclaimable":SReclaimable})

@app.route('/api/loadavg')
def getload(request):
    with open('/proc/loadavg', 'r') as f:
        loadavg = f.read().split()
        loadavg=loadavg[0:3]
        return json.dumps({"loadavg":loadavg})

@app.route('/api/partitions')
def getpart(request):
    with open('/proc/partitions', 'r') as f:
        partitions = [ each.split()[-1] for each in f.readlines()[2:] ]
        Partitions=partitions
        return json.dumps({"partitions":partitions})


resource = app.resource

