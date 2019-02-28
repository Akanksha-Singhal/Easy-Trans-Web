# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 18:54:36 2019

@author: Akanksha Singhal
"""

from Bus import Bus
from Stop import Stop
from Route import Route

# Initializing the stops on a Route
stop1 = Stop(latitude=27.028486, longitude=75.769043, stopname="Todi", stopcode=1000, duration=0, distance =0) 
stop2 = Stop(latitude=26.9181, longitude=75.8498, stopname="Galta Gate", stopcode=1001, duration=20, distance = 5.2)  
stop3 = Stop(latitude=26.9243, longitude=75.8124, stopname="Chandpole", stopcode=1005, duration=10, distance = 3)  
stops = [stop1, stop2, stop3]

#Initializing The Route
r1 = Route("r1", stops)

#Initializing the Buses
bus1 = Bus(busNo = 1)

# Assigning Bus to Routes 
r1.assignBusToRoute(bus1)
r1.startBus(bus1)    

