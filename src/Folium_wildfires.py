#!/usr/bin/env python
# coding: utf-8

# In[41]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
import scipy
## for geospatial
import folium
import geopy

df = pd.read_csv("fire_archive_M6_96619.csv")

city = "Melbourne"
# get location
locator = geopy.geocoders.Nominatim(user_agent="My app") 
city = locator.geocode(city)
location = [city.latitude, city.longitude]
print(city, "\n[lat, long]:", location)

map_ = folium.Map(location=location, tiles="cartodbpositron",
                  zoom_start=8)

# create color column to correspond to type
colors = ["red","yellow","orange", "green"]
indices = sorted(list(df["type"].unique()))
df["color"] = df["type"].apply(lambda x: 
               colors[indices.index(x)])
## scaling the size
scaler = preprocessing.MinMaxScaler(feature_range=(3,15))
df["size"] = scaler.fit_transform(
               df['brightness'].values.reshape(-1,1)).reshape(-1)

df.apply(lambda row: folium.CircleMarker(
           location=[row['latitude'],row['longitude']], 
           popup=row['type'],
           color=row["color"], fill=True,
           radius=row["size"]).add_to(map_), axis=1)

legend_html = """<div style="position:fixed; 
                    top:10px; right:10px; 
                    border:2px solid black; z-index:9999; 
                    font-size:14px;">&nbsp;<b>"""+color+""":</b><br>"""
for i in lst_elements:
     legend_html = legend_html+"""&nbsp;<i class="fa fa-circle 
     fa-1x" style="color:"""+lst_colors[lst_elements.index(i)]+"""">
     </i>&nbsp;"""+str(i)+"""<br>"""
legend_html = legend_html+"""</div>"""
map_.get_root().html.add_child(folium.Element(legend_html))
#plot
map_


# In[ ]:




