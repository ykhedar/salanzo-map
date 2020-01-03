#!/usr/bin/env python
# coding: utf-8

import requests
import math


def build_query(south, west, north, east):
    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = "[out:json];way[\"landuse\"=\"farmland\"](" + str(south) + "," + str(west) + "," + str(
        north) + "," + str(east) + ");(._;>;);out center;"
    return overpass_url, overpass_query


def get_csv_data(url, query):
    response = requests.get(url, params={'data': query})
    data = response.json()
    return [{'id': i['id'], 'lat': i['center']['lat'], 'lon': i['center']['lon']} for i in data['elements'] if i['type'] == 'way']


def getLongLat(bearing, distance, latitude, longitude, reqLatLon):
    R = 6378.1  # Radius of the Earth
    brng = math.radians(bearing)  # Bearing is 90 degrees converted to radians.
    d = distance  # Distance in km

    lat1 = math.radians(latitude)  # Current lat point converted to radians
    lon1 = math.radians(longitude)  # Current long point converted to radians

    lat2 = math.asin(math.sin(lat1) * math.cos(d / R) +
                     math.cos(lat1) * math.sin(d / R) * math.cos(brng))
    lon2 = lon1 + math.atan2(math.sin(brng) * math.sin(d / R) * math.cos(lat1),
                             math.cos(d / R) - math.sin(lat1) * math.sin(lat2))

    if (reqLatLon == "lat"):
        lat2 = math.degrees(lat2)
        return lat2
    elif (reqLatLon == "lon"):
        lon2 = math.degrees(lon2)
        return lon2
    else:
        return "false"


def json_to_csv(data):
    import csv
    # open a file for writing
    employ_data = open('data/test2.csv', 'w')

    # create the csv writer object
    csvwriter = csv.writer(employ_data)

    for emp in data:
        csvwriter.writerow(emp.values())
    employ_data.close()


def get_data(latitude, longitude):
    south = getLongLat(180, 5, latitude, longitude, "lat")
    west = getLongLat(270, 5, latitude, longitude, "lon")
    north = getLongLat(0, 5, latitude, longitude, "lat")
    east = getLongLat(90, 5, latitude, longitude, "lon")
    if south != 'false' and west != 'false' and north != 'false' and east != 'false':
        overpass_url, overpass_query = build_query(south, west, north, east)
        data = get_csv_data(overpass_url, overpass_query)
        json_to_csv(data)
        return data
    else:
        print("returned south or west or north or east as false")
        return False
