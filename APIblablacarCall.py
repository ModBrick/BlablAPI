#
# Created by pcapon on 27/02/18
#

import http.client
import pprint
import json
import requests

def search(start, dest, apikey):

    url = "https://public-api.blablacar.com/api/v2/trips?"

    headers = {
        'accept': "application/json",
        'key': apikey
    }

    params = {
        'fn': start,
        'tn': dest,
        'local': "fr_FR",
        'format': "json"
    }

    print(start, dest)

    resp = requests.get(url=url, params=params, headers=headers)

    print(json.dumps(resp.json(), sort_keys=True, indent=4))

