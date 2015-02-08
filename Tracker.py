# -*- coding: utf-8 -*-

'''
Created on 09.03.2013

@author: raphael
'''
import math
import pygame

class Tracker:
    #Variablen fuer Anzahl Flugzeuge auf Display und insgesamt erstellt
    countPlanes = 0
    ident = 0
    
    def __init__(self, fl, speed, positionX, positionY):
        self.__FL = fl
        self.__Speed = speed
        self.PositionX = positionX
        self.PositionY = positionY
        self.__TrackDataX = self.PositionX
        self.__TrackDataY = self.PositionY
        self.__hist3x = self.PositionX
        self.__hist3y = self.PositionY
        self.__hist2x = self.PositionX
        self.__hist2y = self.PositionY
        self.__hist1x = self.PositionX
        self.__hist1y = self.PositionY
        
        self.__LabelPosition = 0
        
        self.__created = pygame.time.get_ticks()
        
        #Variables for counting aircrafts
        Tracker.countPlanes += 1
        Tracker.ident += 1
        print('Anzahl Flugzeuge: '+str(Tracker.countPlanes))

    def update(self, screen, updateX, updateY, label=True):
        self.__TrackDataX = self.PositionX
        self.__TrackDataY = self.PositionY
        self.PositionX = updateX
        self.PositionY = updateY
        self.drawPosition(screen, self.__TrackDataX, self.__TrackDataY, self.PositionX, self.PositionY, self.__LabelPosition)
        self.history(screen, self.__TrackDataX, self.__TrackDataY)
        
    
    def updateLabelPosition(self):
        self.__LabelPosition = (self.__LabelPosition+1) % 4
        
    def getPosition(self):
        return self.PositionX, self.PositionY
        
    def history(self, screen, newX, newY):
        self.__hist3x = self.__hist2x
        self.__hist3y = self.__hist2y
        self.__hist2x = self.__hist1x
        self.__hist2y = self.__hist1y
        self.__hist1x = newX
        self.__hist1y = newY
        pygame.draw.circle(screen, pygame.Color('black'), (self.__hist1x, self.__hist1y), 2)
        pygame.draw.circle(screen, pygame.Color('black'), (self.__hist2x, self.__hist2y), 2)
        pygame.draw.circle(screen, pygame.Color('black'), (self.__hist3x, self.__hist3y), 2)
        
    def setVector(self, vecX, vecY):
        self.__VecX = vecX
        self.__VecY = vecY
        
    def getVector(self):
        return self.__VecX, self.__VecY
    
    
    #ef getCircle(self, ):
        
        
    def pixelSpeed(self, speed, ratio):
        msSpeed = 16 * speed / 3600000
        return msSpeed 
        
    
        
    
    def drawPosition(self, screen, vorigX, vorigY, positionX, positionY, labelPosition=0, drawLabel=True, abstand=5 ):
        
        if vorigX == positionX and vorigY == positionY:
            pygame.draw.circle(screen, pygame.Color('black'), (vorigX, vorigY), abstand, 1)
        
        else:
            prozentSatz = abstand / (math.sqrt(abs(vorigX-positionX)**2 + abs(vorigY-positionY)**2))
    
            gerundetX = round(abs(vorigX-positionX) * prozentSatz)
            gerundetY = round(abs(vorigY-positionY) * prozentSatz)
    
            if vorigX < positionX and vorigY > positionY:
                PunktCX = int(positionX - gerundetX)
                PunktCY = int(positionY + gerundetY)
        
                PunktBX = int(positionX + gerundetY)
                PunktBY = int(positionY + gerundetX)
        
                PunktAX = int(positionX + gerundetX)
                PunktAY = int(positionY - gerundetY)
        
                PunktDX = int(positionX - gerundetY)
                PunktDY = int(positionY - gerundetX)
        
            if vorigX < positionX and vorigY < positionY:        
                PunktDX = int(positionX - gerundetX)
                PunktDY = int(positionY - gerundetY)
        
                PunktAX = int(positionX + gerundetY)
                PunktAY = int(positionY - gerundetX)
        
                PunktBX = int(positionX + gerundetX)
                PunktBY = int(positionY + gerundetY)
        
                PunktCX = int(positionX - gerundetY)
                PunktCY = int(positionY + gerundetX)
             
            if vorigX > positionX and vorigY < positionY:        
                PunktBX = int(positionX + gerundetX)
                PunktBY = int(positionY - gerundetY)
              
                PunktCX = int(positionX + gerundetY)
                PunktCY = int(positionY + gerundetX)
        
                PunktDX = int(positionX - gerundetX)
                PunktDY = int(positionY + gerundetY)
        
                PunktAX = int(positionX - gerundetY)
                PunktAY = int(positionY - gerundetX)
        
            if vorigX > positionX and vorigY > positionY:
                PunktBX = int(positionX + gerundetX)
                PunktBY = int(positionY + gerundetY)
        
                PunktCX = int(positionX - gerundetY)
                PunktCY = int(positionY + gerundetX)
        
                PunktDX = int(positionX - gerundetX)
                PunktDY = int(positionY - gerundetY)
        
                PunktAX = int(positionX + gerundetY)
                PunktAY = int(positionY - gerundetX)
        
            if vorigX == positionX and vorigY < positionY:        
                PunktAX = positionX
                PunktAY = positionY - abstand
        
                PunktBX = positionX + abstand
                PunktBY = positionY
        
                PunktCX = positionX
                PunktCY = positionY + abstand
        
                PunktDX = positionX - abstand
                PunktDY = positionY
        
            if vorigX == positionX and vorigY > positionY:        
                PunktAX = positionX
                PunktAY = positionY - abstand
        
                PunktBX = positionX + abstand
                PunktBY = positionY
        
                PunktCX = positionX
                PunktCY = positionY + abstand
        
                PunktDX = positionX - abstand
                PunktDY = positionY
    
            if vorigX < positionX and vorigY == positionY:        
                PunktCX = positionX - abstand
                PunktCY = positionY
        
                PunktBX = positionX
                PunktBY = positionY + abstand
        
                PunktAX = positionX + abstand
                PunktAY = positionY
        
                PunktDX = positionX
                PunktDY = positionY - abstand
        
            if vorigX > positionX and vorigY == positionY:
                PunktBX = positionX + abstand
                PunktBY = positionY
        
                PunktCX = positionX
                PunktCY = positionY + abstand
        
                PunktDX = positionX - abstand
                PunktDY = positionY
        
                PunktAX = positionX
                PunktAY = positionY - abstand

            pygame.draw.polygon(screen, pygame.Color('black'), [(PunktAX, PunktAY), (PunktBX, PunktBY), (PunktCX, PunktCY), (PunktDX, PunktDY)], 0)
        
            '''
            schrift = pygame.font.Font('FreeMono.ttf', 12)
            label = schrift.render("A", 1, (0, 0, 255))
            screen.blit(label, (PunktAX, PunktAY))
            
            label = schrift.render("B", 1, (0, 0, 255))
            screen.blit(label, (PunktBX, PunktBY))
            
            label = schrift.render("C", 1, (0, 0, 255))
            screen.blit(label, (PunktCX, PunktCY))
            
            label = schrift.render("D", 1, (0, 0, 255))
            screen.blit(label, (PunktDX, PunktDY))
            '''
        
            
            if drawLabel == True:
                if labelPosition==0:
                    pygame.draw.aaline(screen, pygame.Color('black'), (PunktAX+3, PunktAY-3), (PunktAX+20, PunktAY-20))
                    self.genLabel(screen, 0, PunktAX+20, PunktAY-20)
                if labelPosition==1:
                    pygame.draw.aaline(screen, pygame.Color('black'), (PunktBX+3, PunktBY+3), (PunktBX+20, PunktBY+20))
                    self.genLabel(screen, 1, PunktBX+20, PunktBY+20)
                if labelPosition==2:
                    pygame.draw.aaline(screen, pygame.Color('black'), (PunktCX-3, PunktCY+3), (PunktCX-20, PunktCY+20))
                    self.genLabel(screen, 2, PunktCX-20, PunktCY+20)
                if labelPosition==3:
                    pygame.draw.aaline(screen, pygame.Color('black'), (PunktDX-3, PunktDY-3), (PunktDX-20, PunktDY-20))
                    self.genLabel(screen, 3, PunktDX-20, PunktDY-20)
                    
                    
    def genLabel(self, screen, labelPosition, xEnd, yEnd):
        schrift = pygame.font.Font('FreeMono.ttf', 12)
        if labelPosition==0:
            label1 = schrift.render("DLH123 240", 1, (0, 0, 255))
            label2 = schrift.render("ZEILE 2", 1, (0, 0, 255))
            screen.blit(label1, (xEnd+1, yEnd-24))
            screen.blit(label2, (xEnd+1, yEnd-12))
        if labelPosition==1:
            label1 = schrift.render("DLH123 240", 1, (0, 0, 255))
            label2 = schrift.render("ZEILE 2", 1, (0, 0, 255))
            screen.blit(label1, (xEnd+1, yEnd+1))
            screen.blit(label2, (xEnd+1, yEnd+13))
        if labelPosition==2:
            label1 = schrift.render("DLH123 240", 1, (0, 0, 255))
            label2 = schrift.render("ZEILE 2", 1, (0, 0, 255))
            screen.blit(label1, (xEnd-70, yEnd+1))
            screen.blit(label2, (xEnd-70, yEnd+13))
        if labelPosition==3:
            label1 = schrift.render("DLH123 240", 1, (0, 0, 255))
            label2 = schrift.render("ZEILE 2", 1, (0, 0, 255))
            screen.blit(label1, (xEnd-70, yEnd-24))
            screen.blit(label2, (xEnd-70, yEnd-12))
    
        
    def __del__(self):
        Tracker.countPlanes -= 1