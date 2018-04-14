# coding=utf-8

####################################################################
#                                                                  #
#                     MAIN SCRIPT OF THE DATA BASE                 #
#                            version 1.0                           #
####################################################################

# !/usr/bin/python3
# -*- coding:utf8 -*-

import codecs
import shapefile
import csv
import pyproj




#############################################################################################
# This period is for read the nodes and transform it into the type of a two dimension list
# with the geographic
# In this list, the terms are "id_nodes", "lat", "lon", "id_station", "lat_station", "lon_station",
# #"distance_station", "type_station","number_route", "path1", "path2"
#############################################################################################

myshp = open("NOEUD_ROUTIER.shp", "rb")
mydbf = open("NOEUD_ROUTIER.dbf", "rb")
r = shapefile.Reader(shp=myshp, dbf=mydbf)

neouds = r.shapeRecords()

liste_neoud = []

for i in range(len(neouds)):
    liste = [neouds[i].record[0]] + list(neouds[i].shape.points[0]) + [0,0,0,0,"", 0,0,0] #last "0" is for station
    liste_neoud.append(liste)

print("read nodes finished.....")

#############################################################################################
# This period is for read the routes and transform it into a two dimension list with attributs
# and two points the geographic
# This period is for changing the geographic data of route into the id of the nodes
# And this period will calculate the number of roads for each node, and save the first 2 paths of each node
#############################################################################################

myshp = open("TRONCON_ROUTE.shp", "rb")
mydbf = open("TRONCON_ROUTE.dbf", "rb")
r = shapefile.Reader(shp=myshp, dbf=mydbf)

troncons = r.shapeRecords()

liste_troncon = []


lonth_noeud = len(liste_neoud)

for i in range(10000):
    for j in range(lonth_noeud):

        if (liste_neoud[j][1:3] == list(troncons[i].shape.points[0])):
            id_pointA = liste_neoud[j][0]
            liste_neoud[j][8] += 1
            if (liste_neoud[j][8] == 1): liste_neoud[j][9] = troncons[i].record[0]
            if (liste_neoud[j][8] == 2): liste_neoud[j][10] = troncons[i].record[0]
            break

    for j in range(lonth_noeud):
        if (liste_neoud[j][1:3] == list(troncons[i].shape.points[-1])):
            id_pointB = liste_neoud[j][0]
            liste_neoud[j][8] += 1
            if (liste_neoud[j][8] == 1): liste_neoud[j][9] = troncons[i].record[0]
            if (liste_neoud[j][8] == 2): liste_neoud[j][10] = troncons[i].record[0]
            break

    liste = [troncons[i].record[0]] + list(troncons[i].record[-2:]) + [id_pointA] + [id_pointB]
    liste_troncon.append(liste)

print("read paths finished 1/4.....")

for i in range(10000):
    zone1  = 10000 + i
    for j in range(lonth_noeud):
        zone2 = (j + 8000) % lonth_noeud

        if (liste_neoud[zone2][1:3] == list(troncons[zone1].shape.points[0])):
            id_pointA = liste_neoud[zone2][0]
            liste_neoud[zone2][8] += 1
            if (liste_neoud[zone2][8] == 1): liste_neoud[zone2][9] = troncons[zone1].record[0]
            if (liste_neoud[zone2][8] == 2): liste_neoud[zone2][10] = troncons[zone1].record[0]
            break

    for j in range(lonth_noeud):
        zone2 = (j + 8000) % lonth_noeud
        if (liste_neoud[zone2][1:3] == list(troncons[zone1].shape.points[-1])):
            id_pointB = liste_neoud[zone2][0]
            liste_neoud[zone2][8] += 1
            if (liste_neoud[zone2][8] == 1): liste_neoud[zone2][9] = troncons[zone1].record[0]
            if (liste_neoud[zone2][8] == 2): liste_neoud[zone2][10] = troncons[zone1].record[0]
            break

    liste = [troncons[zone1].record[0]] + list(troncons[zone1].record[-2:]) + [id_pointA] + [id_pointB]
    liste_troncon.append(liste)


print("read paths finished 2/4.....")

for i in range(10000):
    zone1  = 20000 + i
    for j in range(lonth_noeud):
        zone2 = (j + 16000) % lonth_noeud

        if (liste_neoud[zone2][1:3] == list(troncons[zone1].shape.points[0])):
            id_pointA = liste_neoud[zone2][0]
            liste_neoud[zone2][8] += 1
            if (liste_neoud[zone2][8] == 1): liste_neoud[zone2][9] = troncons[zone1].record[0]
            if (liste_neoud[zone2][8] == 2): liste_neoud[zone2][10] = troncons[zone1].record[0]
            break

    for j in range(lonth_noeud):
        zone2 = (j + 8000) % lonth_noeud
        if (liste_neoud[zone2][1:3] == list(troncons[zone1].shape.points[-1])):
            id_pointB = liste_neoud[zone2][0]
            liste_neoud[zone2][8] += 1
            if (liste_neoud[zone2][8] == 1): liste_neoud[zone2][9] = troncons[zone1].record[0]
            if (liste_neoud[zone2][8] == 2): liste_neoud[zone2][10] = troncons[zone1].record[0]
            break

    liste = [troncons[zone1].record[0]] + list(troncons[zone1].record[-2:]) + [id_pointA] + [id_pointB]
    liste_troncon.append(liste)

print("read paths finished 3/4.....")

for i in range(len(troncons) - 30000):
    zone1  = 30000 + i
    for j in range(lonth_noeud):
        zone2 = (j + 24000) % lonth_noeud

        if (liste_neoud[zone2][1:3] == list(troncons[zone1].shape.points[0])):
            id_pointA = liste_neoud[zone2][0]
            liste_neoud[zone2][8] += 1
            if (liste_neoud[zone2][8] == 1): liste_neoud[zone2][9] = troncons[zone1].record[0]
            if (liste_neoud[zone2][8] == 2): liste_neoud[zone2][10] = troncons[zone1].record[0]
            break

    for j in range(lonth_noeud):
        zone2 = (j + 8000) % lonth_noeud
        if (liste_neoud[zone2][1:3] == list(troncons[zone1].shape.points[-1])):
            id_pointB = liste_neoud[zone2][0]
            liste_neoud[zone2][8] += 1
            if (liste_neoud[zone2][8] == 1): liste_neoud[zone2][9] = troncons[zone1].record[0]
            if (liste_neoud[zone2][8] == 2): liste_neoud[zone2][10] = troncons[zone1].record[0]
            break

    liste = [troncons[zone1].record[0]] + list(troncons[zone1].record[-2:]) + [id_pointA] + [id_pointB]
    liste_troncon.append(liste)

print("read paths finished.....")
#############################################################################################
# This periode will delete all the nodes with only two paths
# And put those two paths in one
# Then change the attribut of node who has the relationship with the cancelled patha
# #############################################################################################

delete_noeud = []
delete_path = []
for i in range(len(liste_neoud)):

    if (liste_neoud[i][8] == 2):

        origine_path1 = liste_neoud[i][9]
        origine_path2 = liste_neoud[i][10]

        index_path1 = int(origine_path1 - 1)
        index_path2 = int(origine_path2 - 1)

        if (index_path1 > 8099): index_path1 = index_path1 - 1
        if (index_path2 > 8099): index_path2 = index_path2 - 1

        if (liste_troncon[index_path1][3] == liste_neoud[i][0]):
            if (liste_troncon[index_path2][3] == liste_neoud[i][0]):
                path1 = liste_troncon[index_path2][4]
            else:
                path1 = liste_troncon[index_path2][3]
            liste_troncon[index_path1][3] = path1


        else:
            if (liste_troncon[index_path2][3] == liste_neoud[i][0]):
                path1 = liste_troncon[index_path2][4]
            else:
                path1 = liste_troncon[index_path2][3]
            liste_troncon[index_path1][4] = path1


        if (liste_neoud[path1 - 1][9] == origine_path2):

            liste_neoud[path1 - 1][9] = origine_path1


        if (liste_neoud[path1 - 1][10] == origine_path2):

            liste_neoud[path1 - 1][9] = origine_path1

        liste_troncon[index_path1][2] += liste_troncon[index_path2][2]


        delete_noeud.append(i)
        delete_path.append(index_path2)

for i in range(len(delete_noeud)):
    liste_neoud[delete_noeud[i]] = ''

for i in range(len(delete_path)):
    liste_troncon[delete_path[i]] = ''

while '' in liste_neoud:
    liste_neoud.remove('')
while '' in liste_troncon:
    liste_troncon.remove('')

print("data has already been cleaned")

# #############################################################################################
#  This period is for read a csv file of the stations
#  Put the geograph into lam-93
#  And put them into a list
# #############################################################################################

csvFile = open("IRVE-201605.csv", "r", encoding="utf8")
reader = csv.reader(csvFile)


station = []
list_stations = []
for item in reader:
    station = [item[0]] + item[3:5] + [item[6]]
    list_stations.append(station)

list_stations.pop(0)

wgs84 = pyproj.Proj('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')
lambert = pyproj.Proj('+proj=lcc +lat_1=49 +lat_2=44 +lat_0=46.5 +lon_0=3 +x_0=700000 +y_0=6600000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs')

for i in range(len(list_stations)):
    list_stations[i][1], list_stations[i][2] = pyproj.transform(wgs84, lambert, list_stations[i][1], list_stations[i][2])
    print(list_stations[i])







#############################################################################################
# This period is for put the data in a csv
# And with the correct name
#############################################################################################

fileHeader1 = ["id_noeud", "lat", "lon", "id_station", "lat_station", "lon_station", "distance_station", "type_station","number_route", "path1", "path2"]
fileHeader2 = ["id_route", "type_route", "distance", "id_noeud1", "id_noeud2"]
csvFile = open("Liste_noeud.csv", "w", newline ='')


writer = csv.writer(csvFile)

writer.writerow(fileHeader1)
for i in range(len(liste_neoud)):
    writer.writerow(liste_neoud[i])

csvFile.close()



csvFile = open("Liste_routes.csv", "w", newline ='')

writer = csv.writer(csvFile)

writer.writerow(fileHeader2)
for i in range(len(liste_troncon)):
    writer.writerow(liste_troncon[i])

csvFile.close()
