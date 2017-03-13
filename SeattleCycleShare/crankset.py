#!/usr/local/venv/SeattleCycle/bin/python3

import pandas as pd 
import time as tm

t0 = tm.time()                              # time 

df_sta = pd.read_csv('/usr/local/venv/SeattleCycle/data/station.csv')

df_weather = pd.read_csv('/usr/local/venv/SeattleCycle/data/weather.csv')

df_trips = pd.read_csv('/usr/local/venv/SeattleCycle/data/trip.csv',
                      skiprows=[50793])

t1 = tm.time()                              # time 

df_num_tr = pd.DataFrame(index=df_sta.station_id,
                columns=df_sta.station_id)  # not controlling for weather

t2 = tm.time()                              # time 



for i in df_sta.station_id:                 # from
    for j in df_sta.station_id:             # to 
        df_num_tr[i][j] = len(df_trips[(df_trips.from_station_id==i) & 
        (df_trips.to_station_id==j)].trip_id)


t3 = tm.time()                              # time 

print(t3-t0)                                # 113.09097003936768
print(t3-t2)                                # 112.04273104667664

# ...........................................................

pd.unique(df_trips.gender)
pd.unique(df_trips.usertype)

df_trips_m = df_trips[df_trips.gender=='Male']      # 140,564
df_trips_f = df_trips[df_trips.gender=='Female']    #  37,562

len(df_trips[df_trips.gender=='Male'])


df_tr_gender = df_trips.groupby(['Gender']) 


df_trips.groupby('gender').count()

# ...........................................................
# ...........................................................


# from_sta = df_trips.groupby('from_station_id')


""" 
goals  - - - - - - - - - - - - - - - - - 
matrix with df_sta.station_id as row and column names & values counting trips

notes - - - - - - - - - - - - - - - - - - 


sta = df_sta.station_id                     # station list, for clarity


for i in sta:                               # from
    for j in sta:                           # to 
        xxx[i][j] = len(df_trips[(df_trips.from_station_id==i) & 
        (df_trips.to_station_id==j)].trip_id)



max(xxx['BT-01'])
Out[151]: 1247


xxx[sta[0]][sta[0]] = len(df_trips[(df_trips.from_station_id==sta[0]) & 
    (df_trips.to_station_id==sta[0])].trip_id)
    
xxx[sta[0]][sta[1]] = len(df_trips[(df_trips.from_station_id==sta[0]) & 
    (df_trips.to_station_id==sta[1])].trip_id)
    
xxx[sta[0]][sta[2]] = len(df_trips[(df_trips.from_station_id==sta[0]) & 
    (df_trips.to_station_id==sta[2])].trip_id)

for i in sta:
    xxx[i][sta[0]] = len(df_trips[(df_trips.from_station_id==i) & 
    (df_trips.to_station_id==sta[0])].trip_id)
    
    

xxx['BT-01']['BT-01']
Out[133]: nan

sta[0]
Out[134]: 'BT-01'

xxx[sta[0]][sta[0]]
Out[135]: nan



df_bt01 = df_trips[df_trips.from_station_id=='BT-01']

len(df_bt01.from_station_id)

Out[46]: 10934

pd.unique(df_sta.name)



# ...........................................................
 
df_bt01 = df_trips[df_trips.from_station_id=='BT-01']
    #,tostationid=='BT-03'

len(pd.unique(df_bt01.to_station_id))   # 57
len(df_sta.station_id)                  # 58

len(df_bt01[df_bt01.to_station_id=='BT-01'])

df_1_3 = df_bt01[(df_bt01.from_station_id=='BT-01') & 
    (df_bt01.to_station_id=='BT-03')]

# ...........................................................

df_1_3__2 = df_trips[(df_trips.from_station_id=='BT-01') & 
    (df_trips.to_station_id=='BT-03')]

df_1_3__3 = df_trips[(df_trips.from_station_id==sta[0]) & 
    (df_trips.to_station_id==sta[1])]



- - - - - - - - - - - - - - - - - - - - - 
"""