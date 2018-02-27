#
# Created by pcapon on 27/02/18
#

import argparse
import APIblablacarCall


class tripclass:
    '''Class for keeping track of an item in inventory.'''
    Sstart: str
    Sdest: str

    def __str__(self):
        return "{} -> {}".format(self.Sstart.decode('utf8'), self.Sdest.decode('utf8'))

    def __repr__(self):
        return str(self)


class blablApi:

    def __init__(self, filetripname, apikey):
        self.triplist = self.getTrip(filetripname)
        self.apikey = apikey
        print(self.triplist)

    def searchTrajet(self):
        for trip in self.triplist:
            APIblablacarCall.search(trip.Sstart, trip.Sdest, self.apikey)

    def getTrip(self, filetripname):
        triplist = []
        filetrip = open(filetripname, "r")
        trips = filetrip.read().splitlines()
        for trip in trips:
            trip_class = tripclass()
            startdest = trip.split('|')
            trip_class.Sstart = startdest[0].encode('utf8')
            trip_class.Sdest = startdest[1].encode('utf8')
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
