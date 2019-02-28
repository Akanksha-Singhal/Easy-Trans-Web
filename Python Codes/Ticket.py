# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 22:43:31 2019

@author: Akanksha Singhal
"""

class Ticket():
    
    def __init__(self, noOfAdultMales, noOfAdultFemales, noOfMaleStudents, noOfFemaleStudents, noOfChildren, startStop, endStop):
        self.noOfAdultMales = noOfAdultMales
        self.noOfAdultFemales = noOfAdultFemales
        self.noOfMaleStudents = noOfMaleStudents
        self.noOfFemaleStudents = noOfFemaleStudents
        self.noOfChildren = noOfChildren
        self.startStop = startStop
        self.endStop = endStop
        self.totalFare = 0
        self.distance = endStop.distance
        self.calculateFare()   
        
        
    def calculateFare(self):
        self.fare = 0.9*self.distance;
        self.totalFare = self.noOfAdultMales*self.fare
        self.totalFare += self.noOfAdultFemales*self.fare*0.75
        self.totalFare += self.noOfMaleStudents*self.fare*0.5
        self.totalFare += self.noOfFemaleStudents*self.fare*0.75*0.5
        self.totalFare += self.noOfChildren*self.fare*0.5
        self.totalFare = round(self.totalFare, 2)
        
    def showTicket(self):
        print('Ticket :')
        print('SS: ',self.startStop.stopcode,' (',self.startStop.stopname,')')
        print('ES: ',self.endStop.stopcode, '(', self.endStop.stopname,')')
        print('MA: ',self.noOfAdultMales)
        print('FA: ',self.noOfAdultFemales)
        print('SM: ',self.noOfMaleStudents)
        print('SF: ',self.noOfFemaleStudents)
        print('C : ',self.noOfChildren)
        print('AMT:',self.totalFare)
    