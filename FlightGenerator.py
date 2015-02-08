# -*- coding: utf-8 -*-

'''
Created on 10.03.2013

@author: raphael
'''

import random
import pygame
import math

class FlightGenerator:
    
    def __init__(self):
        self.FlightID = "DLH 123"
        self.speed = 400
    
    def generateFlight(self):
        
        #N=0 O=1 S=2 W=3
        fromDirection = random.randint(0, 3)
        print(str(fromDirection))
        entryX = 0
        entryY = 0
        directX = 0
        directY = 0
        
        
        if fromDirection == 0:
            entryX = random.randint(20, (pygame.display.Info().current_w-20))
            entryY = 0
            
            directX = random.randint(20, pygame.display.Info().current_w-20) #entryX+5
            directY = random.randint(20, pygame.display.Info().current_h-20) #450
            print('Neuer Abflug auf '+str(entryX)+' '+str(entryY))
        elif fromDirection == 1:
            entryX = pygame.display.Info().current_w
            entryY = random.randint(20, pygame.display.Info().current_h-20)
            
            directX = random.randint(20, pygame.display.Info().current_w-20) #5
            directY = random.randint(20, pygame.display.Info().current_h-20) #entryY+5
            print('Neuer Abflug auf '+str(entryX)+' '+str(entryY))
        elif fromDirection == 2:
            entryX = random.randint(20, pygame.display.Info().current_w-20)
            entryY = random.randint(20, pygame.display.Info().current_h-20) #pygame.display.Info().current_h
            
            directX = random.randint(20, pygame.display.Info().current_w-20) #entryX+5
            directY = random.randint(20, pygame.display.Info().current_h-20) #5
            print('Neuer Abflug auf '+str(entryX)+' '+str(entryY))
        elif fromDirection == 3:
            entryX = 0
            entryY = random.randint(20, pygame.display.Info().current_h-20)
            
            directX = random.randint(20, pygame.display.Info().current_w-20) #450
            directY = random.randint(20, pygame.display.Info().current_h-20) #entryY+5
            print('Neuer Abflug auf '+str(entryX)+' '+str(entryY))
        
        print(str(entryX)+' '+str(entryY)+' '+str(directX)+' '+str(directY))
        change = self.genDirection(entryX, entryY, directX, directY)    
        return entryX, entryY, change[0], change[1]
    
    def genDirection(self, entryX, entryY, directX, directY, speed=15):
        prozentSatz = speed / (math.sqrt(abs(entryX-directX)**2 + abs(entryY-directY)**2))
        
        gerundetX = int(round(abs(entryX-directX) * prozentSatz))
        gerundetY = int(round(abs(entryY-directY) * prozentSatz))
        print('Gerundet: '+str(gerundetX)+' '+str(gerundetY))
        if entryX < directX and entryY < directY:
            return gerundetX, gerundetY
        if entryX < directX and entryY > directY:
            return gerundetX, -gerundetY
        if entryX > directX and entryY < directY:
            return -gerundetX, -gerundetY
        if entryX > directX and entryY > directY:
            return -gerundetX, gerundetY
        