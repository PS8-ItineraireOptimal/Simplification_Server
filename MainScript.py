####################################################################
#                                                                  #
#                     MAIN SCRIPT OF THE DATA BASE                 #      
#                            version 1.0                           #
####################################################################


import shapefile
import pandas as pd

#############################################################################################
# This periode is for read the noeuds and transform it into the type of a two dimension list 
# with the geographic    
# In this list, the terms are noeud_id, type_noeud, nothing, lat, lon, station
#############################################################################################

myshp = open("NOEUD_ROUTIER.shp", "rb")
mydbf = open("NOEUD_ROUTIER.dbf", "rb")
r = shapefile.Reader(shp=myshp, dbf=mydbf)

neouds = r.shapeRecords()

liste_neoud = []

for i in range(len(neouds)):
    liste = neouds[i].record[:] + list(neouds[i].shape.points[0]) + [0] #last "0" is for station
    liste_neoud.append(liste)

#############################################################################################
# This periode is for read the routes and transform it into a two dimension list with attributs
# and two points the geographic
#############################################################################################

myshp = open("TRONCON_ROUTE.shp", "rb")
mydbf = open("TRONCON_ROUTE.dbf", "rb")
r = shapefile.Reader(shp=myshp, dbf=mydbf)

troncons = r.shapeRecords()
shape = r.shapes()

for name in dir(shape[3]):
      if not name.startswith('__'):
        print(name)

print(r.shapeType)

#############################################################################################
# This periode is for change the geographic data of route into the id of the noeuds
#############################################################################################
