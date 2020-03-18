import json
import os
from azat import ROOT_DIR

BASE_URL =os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath('__file__'))))
# def logCurrent(key,telephone):
def logCurrent(key,telephone):
    current = {'key':key,'telephone':telephone}
    jdata = json.dumps(current)
    with open(os.path.join(ROOT_DIR,'log/current.json'),'w') as jfile:
        jfile.write(jdata)
    # src = os.path.join(BASE_URL,'log/current.json')
    return None




