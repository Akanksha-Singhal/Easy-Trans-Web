# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 17:16:28 2019

@author: Akanksha Singhal
"""
import datetime
from Bus import Bus


class Route():
    
    def __init__(self, routeNo, stops):
        self.routeNo = routeNo
        self.stops = stops
        self.buses = []
        
    def assignBusToRoute(self, bus):
        self.buses.append(bus)
        bus.assignRoute(self)
        
    def startBus(self, bus):
        currentDT = datetime.datetime.now()
        bus.startTime = currentDT.strftime("%H:%M:%S")
        print("Bus ", bus.busNo, ' starts on Route No: ', self.routeNo, 'at time : ', bus.startTime)
        bus.start()  
    
        
        