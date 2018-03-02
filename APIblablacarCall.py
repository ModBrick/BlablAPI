#
# Created by pcapon on 27/02/18
#

import http.client
import pprint
import json
import requests



def search(start, dest, page, apikey):
    '''Search and return JSON.'''

    url = "https://public-api.blablacar.com/api/v2/trips?"

    headers = {
        'accept': "application/json",
        'key': apikey
    }

    params = {
        'fn': start,
        'tn': dest,
        'page': page,
        'local': "fr_FR",
        'format': "json"
    }

    print(start, dest)

    resp = requests.get(url=url, params=params, headers=headers)
    #print(json.dumps(resp.json(), sort_keys=True, indent=4))
    return resp.json()

    #print(json.dumps(pagerjson, sort_keys=True, indent=4))

def jsonPrint(jsonstring):
    print(json.dumps(jsonstring, sort_keys=True, indent=4))

def getInfo():
    """TODO"""