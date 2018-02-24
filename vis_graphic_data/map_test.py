import pandas as pd
import numpy as py
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

#画一个大弧线，大弧线用于在地球球体上定位两个点的弧线，一般用于航线
def create_great_circles(dataFrame):
    ite_rows = dataFrame.iterrows()
    for index, item in ite_rows:
        if(abs(item['end_lat'] - item['start_lat']) < 180
           and abs(item['end_lat'] - item['start_lat']) < 180) :
            m.drawgreatcircle(item['start_lon'], item['start_lat'], item['end_lon'], item['end_lat'])

airlines = pd.read_csv("airlines.csv")
airports = pd.read_csv("airports.csv")
routes = pd.read_csv("routes.csv")
geo_routes = pd.read_csv("geo_routes.csv")

#basemap constructor, create instance
m = Basemap(projection = 'merc', llcrnrlat = -80, urcrnrlat = 80, llcrnrlon = -180, urcrnrlon = 180)
# #Draw coast lines
m.drawcoastlines()

#Get lon & lat from csv file
# airport_lon = airports['longitude'].tolist()
# airport_lat = airports['latitude'].tolist()
#
# print(airport_lon[0: 5])
#
# #Convert coordinate to what we want
# x, y = m(airport_lon, airport_lat)
# # print(x[0: 5])
#
# #结合plt，设置画布大小及title
# fig, ax = plt.subplots(figsize=(15,20))
#
# #Display a simple scatter
# m.scatter(x, y, s = 1)
#
# plt.title('Scaled Up Earth With Coastlines')
# plt.show()

dfw = geo_routes[geo_routes['source'] == 'DFW']
create_great_circles(dfw)
plt.show()

