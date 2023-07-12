#!/usr/bin/env python
# coding: utf-8

# In[8]:


get_ipython().system('pip install requests')
get_ipython().system('pip install matplotlib')


# In[ ]:


import requests
import time
json = "http://api.open-notify.org/iss-now.json"
dp = []
for i in range(100):
    res = requests.get(json)
    if response.status_code == 200:
        data = response.json()
        timestamp = data["timestamp"]
        lat = float(data["iss_position"]["latitude"])
        long = float(data["iss_position"]["longitude"])
        dp.append((long, lat, timestamp))
    time.sleep(10) 


# In[38]:


longitudes = [point[0] for point in dp]
latitudes = [point[1] for point in dp]

# Plot the ISS path as a line graph
plt.plot(longitudes, latitudes)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Path of the International Space Station')
plt.grid(True)
plt.show()

