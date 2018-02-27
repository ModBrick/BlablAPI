#
# Created by pcapon on 27/02/18
#

import http.client
import pprint

def search(start, dest, apikey):

    conn = http.client.HTTPSConnection("public-api.blablacar.com")

    headers = {
        'accept': "application/json",
        'key': apikey
    }

    print(start, dest)

    conn.request("GET",
                 "/api/v2/trips?fn={}&tn={}&locale=fr_FR&_format=xml".format(start, dest),
                 headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))