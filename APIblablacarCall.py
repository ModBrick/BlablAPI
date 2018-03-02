#
# Created by pcapon on 27/02/18
#

import http.client
import pprint
import json
import requests

def trajetSuggestion(start, dest):
    url = "https://www.blablacar.fr/publication/suggestions?"

    params = {
        'from': start,
        'to': dest
    }

    resp = requests.get(url=url, params=params)
    print(resp.json())


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

def getInfo(Trip_ID, apikey, locale="fr_FR", format="json"):
    """TODO"""

    url = "https://public-api.blablacar.com/api/v2/trips/"
    url += "{}?".format(Trip_ID)

    headers = {
        'accept': "application/json",
        'key': apikey
    }

    params = {
        'locale': locale,
        '_format': format
    }

    resp = requests.get(url=url, params=params, headers=headers)
    return (resp.json())