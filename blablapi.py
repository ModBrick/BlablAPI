#
# Created by pcapon on 27/02/18
#

import argparse

import time

import APIblablacarCall
import json



class tripclass:
    '''Class for keeping track of an item in inventory.'''
    def __init__(self, Sstart, Sdest):
        self.Sstart = Sstart
        self.Sdest = Sdest

    def __str__(self):
        return "{} -> {}".format(self.Sstart.decode('utf8'), self.Sdest.decode('utf8'))

    def __repr__(self):
        return str(self)

class infotrip:
    def __init__(self):
        


class blablApi:

    def __init__(self, filetripname, apikey):
        self.triplist = self.getTripList(filetripname)
        self.apikey = apikey
        print(self.triplist)

    def searchTrajet(self):
        for trip in self.triplist:
            jsonsearch = APIblablacarCall.search(trip.Sstart, trip.Sdest, 1, self.apikey)
            #APIblablacarCall.jsonPrint(jsonsearch)
            if jsonsearch['pager']['pages'] > 1:
                self.pageToPage(trip, jsonsearch)
            else:
                self.getTripId(jsonsearch)

    def getTripId(self, json):
        trips = json['trips']
        for trip in trips:
            #APIblablacarCall.jsonPrint(trip)
            self.getTrajetSuggestions(trip)
            id = trip['permanent_id']
            jsontrip = APIblablacarCall.getInfo(id, self.apikey)
            # TODO: WRITE HERE INFO TRIP
            print('============================================================================================')

    def getTrajetSuggestions(self, jsontrip):
        destpos = str(jsontrip['arrival_place']['latitude']) + "," + str(jsontrip['arrival_place']['longitude'])
        deppos = str(jsontrip['departure_place']['latitude']) + "," + str(jsontrip['departure_place']['longitude'])

        suggjson = APIblablacarCall.trajetSuggestion(deppos, destpos)
        for label in suggjson:
            print(label['label'])
        APIblablacarCall.jsonPrint(suggjson)



    def pageToPage(self, trip, jsonsearch):
            while int(jsonsearch['pager']['page']) < int(jsonsearch['pager']['pages']):
                print("{}/{}".format(jsonsearch['pager']['page'], jsonsearch['pager']['pages']))
                self.getTripId(jsonsearch)
                page = jsonsearch['pager']['page']
                page += 1
                jsonsearch = APIblablacarCall.search(trip.Sstart, trip.Sdest, page, self.apikey)

    def getTripInfo(self, jsontrip):
        """TODO"""

    def getTripList(self, filetripname):
        triplist = []
        filetrip = open(filetripname, "r")
        trips = filetrip.read().splitlines()
        for trip in trips:
            startdest = trip.split('|')
            trip_class = tripclass(startdest[0].encode('utf8'), startdest[1].encode('utf8'))
            triplist.append(trip_class)
        return (triplist)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filetrip', metavar='f',
                        help='File with trip')
    parser.add_argument('apikey', metavar='a',
                        help='API key')

    args = parser.parse_args()
    blabla = blablApi(args.filetrip, args.apikey)
    blabla.searchTrajet()


if __name__ == "__main__":
    main()
