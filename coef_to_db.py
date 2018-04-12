########################################################################################################################
#                                                                                                                      #
# This python script feeds the dataBase in five steps every n minutes:                                                 #
#       - The projet_S8 database is store into BACKUP folder in a SQL file: backup_projet_S8(date).sql                 #
#       - A EV list is created with manufactures characteristic                                                        #
#       - Nodes and roads csv files is transform into data frame and clean                                             #
#       - The coefficients are computed                                                                                #
#       - projet_S8 database is updated by those new data frame                                                        #
#                                                                                                                      #
# Techno: linux server ubuntu 16.04, python 3.5.2, MySQL, crontab, Raspberry Pi                                        #
#                                                                                                                      #
# Library to install: sqlalchemy, numpy, pandas and subprocess                                                         #
#                                                                                                                      #
########################################################################################################################

from sqlalchemy import create_engine    # Library to connect the DB
import random                           # Library for random number
import numpy as np                      # Library with array functions
import pandas as pd                     # Library for create data frame
import subprocess                       # Library for uses the shell cmd

########################################################################################################################
#                                       Step one: BACKUP projet_S8 database                                            #
########################################################################################################################
subprocess.run('mysqldump -hlocalhost -pprojets8 -uroot projet_S8 > BACKUP/backup_projet_S8_$(date).sql', shell=True)

########################################################################################################################
#                                       Step two: EV list created                                                      #
########################################################################################################################
index = pd.Series(["Renault","Renault","Renault","Renault","Tesla","Tesla",
                   "Citroen","Bollore","Smart","Nissan","Ford","Opel"
                  ],
                  ["Zoe","Fluence","Kangoo","Twizi","Roadster","S",
                   "C-Zero","Bluecar","Fortwo","Leaf","Focus","Ampera"
                  ])

df = pd.DataFrame({ 'Marque' : index})
df["kWh100km"] = (10.5,11.9,12.9,5.08,15.1,19.9,10.7,12,12.1,13.7,14.375,14)
df["Battery"] = (14.2,22,22,6.1,53,85,16,30,17.6,24,23,16)

########################################################################################################################
#                                       Step three: open and clean the csv files into a data frame                     #
########################################################################################################################
df_nodes = pd.read_csv('Liste_noeud.csv', sep=',')
df_roads = pd.read_csv('Liste_routes.csv', sep=',')

# Delete unused columns
df_nodes = df_nodes.drop("path1",1)
df_nodes = df_nodes.drop("path2",1)
df_nodes = df_nodes.drop("number_route",1)

# Change the type_route to a speed limit
df_roads["type_route"] = df_roads["type_route"].replace(["b'D\\xe9partementale'"], 90)
df_roads["type_route"] = df_roads["type_route"].replace(["Autoroute"], 130)
df_roads["type_route"] = df_roads["type_route"].replace(["Sans objet"], 50)
df_roads["type_route"] = df_roads["type_route"].replace(["Nationale"], 90)
df_roads = df_roads.rename(columns={"type_route":"vitesse"})

# Create a random number between 0 and 1, which represent the traffic congestion and weather
df_roads["random"] = np.random.uniform(0,1, size=len(df_roads))

########################################################################################################################
#                                       Step four: calculation of coefficients Tij and Eij                             #
########################################################################################################################
df_roads["Eij kWh"] = df["kWh100km"].mean()*df_roads["distance"]/100
df_roads["Tij h"] = df_roads["distance"]/(df_roads["vitesse"]*df_roads["random"])
df_roads = df_roads.drop("random",1)
########################################################################################################################
#                                       Step five: connection to mysql and update tables                               #
########################################################################################################################
engine = create_engine('mysql+mysqlconnector://root:projets8@localhost/projet_S8')

df_roads.to_sql(con=engine, if_exists='replace', index=False, name="roads")
df_nodes.to_sql(con=engine, if_exists='replace', index=False, name="nodes")
df.to_sql(con=engine, if_exists='replace', index=False, name="car")
engine.dispose()
