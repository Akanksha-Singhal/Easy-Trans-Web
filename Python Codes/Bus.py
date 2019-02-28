# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 15:28:10 2019

@author: Akanksha Singhal
"""

from Ticket import Ticket

import threading
import time
import numpy as np
import random

class Bus(threading.Thread):
    maxPassengers = 50
    def __init__(self, busNo):
        threading.Thread.__init__(self)
        self.busNo = busNo
        self.totalPassengers = 0
        self.boardingPassengers = []
        self.alightingPassengers = []
        self.tickets = []
        
        self.route = None
        
        #self.startStop = None
        #self.endStop = None
        #self.curr_latitude = None
        #self.curr_longitude = None        
        
        self.curr_stop = 0
        self.startTime = None 
        self.runningStatus = False  
    
    def assignRoute(self, route):
        self.route = route
        self.boardingPassengers  = list(np.zeros(len(self.route.stops), dtype=int))
        self.alightingPassengers = list(np.zeros(len(self.route.stops), dtype=int))
        
    
    def getStopStatus(self):
        
        print('Current stop is '+ self.route.stops[self.curr_stop].stopname)
        if self.curr_stop < len(self.route.stops)-1:
            print('Next stop will be ', self.route.stops[self.curr_stop+1].stopname,' in ',self.route.stops[self.curr_stop+1].duration, ' minutes')
        else:
            print('This is the final stop.')
            
    def generateTickets(self):
        #nextStops = self.route.stops[self.curr_stop+1:]
        #probability of selecting NextStop 
        #probNextStop = np.ones(len(nextStops))
        
        #Select the no Of passengers to board on current Stop
        noOfPassengers = random.randint(0, 10)
        
        NoOfPassengersFromCurStop=0
        while( NoOfPassengersFromCurStop < noOfPassengers):
            
            currentTicketPassengers = 0
            # passengers boarding from current stop
            noOfAdultMales = random.randint(0, 2)
            noOfAdultFemales = random.randint(0, 2)
            noOfMaleStudents = random.randint(0, 3)
            noOfFemaleStudents = random.randint(0, 2)
            noOfChildren = random.randint(0, 2)
            startStop = self.route.stops[self.curr_stop]            
            endStopNo = random.randint(self.curr_stop+1, len(self.route.stops)-1)
            endStop = self.route.stops[endStopNo] 
            
            # create a Ticket
            t=Ticket(noOfAdultMales, noOfAdultFemales, noOfMaleStudents, noOfFemaleStudents, noOfChildren, startStop, endStop )
            self.tickets.append(t)
            t.showTicket()
            
            #No of passengers boarding on current Stop
            currentTicketPassengers += noOfAdultMales + noOfAdultFemales + noOfMaleStudents + noOfFemaleStudents + noOfChildren
            NoOfPassengersFromCurStop += currentTicketPassengers 
            
            #Recording how many passengers will deboard at upcoming stops
            self.alightingPassengers[endStopNo] += currentTicketPassengers 
            
        self.totalPassengers += NoOfPassengersFromCurStop              
        self.boardingPassengers[self.curr_stop] = NoOfPassengersFromCurStop
            
        
    def deboardPassengers(self):
        print(self.alightingPassengers[self.curr_stop],' of passengers have deboarded.')
        self.totalPassengers -= self.alightingPassengers[self.curr_stop] 
        
        
            
    def boardPassengers(self):
        if((self.curr_stop != len(self.route.stops)-1) and (self.totalPassengers < self.maxPassengers )):
            print('passengers boarding..')
            self.generateTickets()
            print(self.boardingPassengers[self.curr_stop],' of passengers boarded.')
            print(' total no of passengers',self.totalPassengers)
            
        elif(self.totalPassengers >= self.maxPassengers):
            print('Bus full.. no more passengers can board')
        
    def waitTillNextStop(self):        
        if(self.curr_stop != len(self.route.stops)-1):
            print('bus is running \n')
            time.sleep(self.route.stops[self.curr_stop+1].duration)
        self.curr_stop = self.curr_stop+1
        
    def run(self):
        self.runningStatus = True
        print('Bus started..')
        
        while(self.curr_stop != len(self.route.stops)):
            self.getStopStatus()
            self.deboardPassengers()
            self.boardPassengers()
            self.waitTillNextStop()    
        
        print('Bus stops..')


