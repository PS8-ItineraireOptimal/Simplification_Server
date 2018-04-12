import random
import numpy as np
import pandas as pd

##### Import roads and nodes csv files
df_nodes = pd.read_csv('Liste_noeud.csv', sep=',')
df_roads = pd.read_csv('Liste_routes.csv', sep=',')

##### Creation of the EV list
index = pd.Series(["Renault","Renault","Renault","Renault",
                  "Tesla","Tesla","Citroen","Bollore","Smart",
                  "Nissan","Ford","Opel"],
                  ["Zoe","Fluence","Kangoo","Twizi","Roadster",
                   "S","C-Zero","Bluecar","Fortwo","Leaf",
                   "Focus","Ampera"])
df = pd.DataFrame({ 'Marque' : index})
df["kWh/100km"] = (10.5,11.9,12.9,5.08,15.1,19.9,10.7,12,12.1,13.7,14.375,14)
df["Battery"] = (14.2,22,22,6.1,53,85,16,30,17.6,24,23,16)

##### Change the type_route to a speed limit
df_roads["type_route"] = df_roads["type_route"].replace(["b'D\\xe9partementale'"], 90)
df_roads["type_route"] = df_roads["type_route"].replace(["Autoroute"], 130)
df_roads["type_route"] = df_roads["type_route"].replace(["Sans objet"], 50)
df_roads["type_route"] = df_roads["type_route"].replace(["Nationale"], 90)
df_roads = df_roads.rename(columns={"type_route":"vitesse"})

##### Create a random number between 0 and 1, which represent the traffic congestion and weather
df_roads["random"] = np.random.uniform(0,1, size=len(df_roads))

##### Compute Eij
df_roads["Eij (kWh)"] = df["kWh/100km"].mean()*df_roads["distance"]/100

# Compute Tij
df_roads["Tij (h)"] = df_roads["distance"]/(df_roads["vitesse"]*df_roads["random"])