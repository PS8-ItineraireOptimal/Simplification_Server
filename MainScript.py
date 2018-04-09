import shapefile
import pandas as pd

myshp = open("NOEUD_ROUTIER.shp", "rb")
mydbf = open("NOEUD_ROUTIER.dbf", "rb")
r = shapefile.Reader(shp=myshp, dbf=mydbf)
# 在输出的记录中找到经纬度, 假设经纬度分别是第三四个属性

neouds = r.shapeRecords()

liste_neoud = []

for i in range(len(neouds)):
    liste = neouds[i].record[:] + list(neouds[i].shape.points[0])
    liste_neoud.append(liste)



myshp = open("TRONCON_ROUTE.shp", "rb")
mydbf = open("TRONCON_ROUTE.dbf", "rb")
r = shapefile.Reader(shp=myshp, dbf=mydbf)

troncons = r.shapeRecords()
shape = r.shapes()

for name in dir(shape[3]):
      if not name.startswith('__'):
        print(name)

print(r.shapeType)