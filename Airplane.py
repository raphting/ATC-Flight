# -*- coding: utf-8 -*-

'''
Created on 09.03.2013

@author: raphael
'''
class Airplane():
    airplane_counter = 0
    
    def __init__(self, typ, callsign, fl, speed, positionX, positionY, destX, destY):
        self.__Typ = typ
        self.__Callsign = callsign
        self.__FL = fl
        self.__Speed = speed
        self.__PositionX = positionX
        self.__PositionY = positionY
        self.__DestX = destX
        self.__DestY = destY
        self.airplane_counter += 1
        
    def getCallsign(self):
        return self.__Callsign
        
    def setFL(self, fl):
        self.__FL = fl
        
    def getFL(self):
        return self.__FL
    
    def setSpeed(self, speed):
        self.__Speed = speed
        
    def getSpeed(self):
        return self.__Speed        
        
    def setPosition(self, positionX, positionY):
        self.__PositionX = positionX
        self.__PositionY = positionY
        
    def getPosition(self):
        return (self.__PositionX, self.__PositionY)
    
    def getDestination(self):
        return (self.__DestX, self.__DestY)
    
    def __del__(self):
        self.airplane_counter -= 1