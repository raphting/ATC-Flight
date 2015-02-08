# -*- coding: UTF-8 -*-
 
# Pygame-Modul importieren.
import pygame
import time
from Airplane import Airplane
from Tracker import Tracker
from FlightGenerator import FlightGenerator
 
# Überprüfen, ob die optionalen Text- und Sound-Module geladen werden konnten.
if not pygame.font: print('Fehler pygame.font Modul konnte nicht geladen werden!')
if not pygame.mixer: print('Fehler pygame.mixer Modul konnte nicht geladen werden!')
 
def main():
    # Initialisieren aller Pygame-Module und    
    # Fenster erstellen (wir bekommen eine Surface, die den Bildschirm repräsentiert).
    pygame.init()
    pygame.font.init()
        
    screen = pygame.display.set_mode((800, 600))
 
    # Titel des Fensters setzen, Mauszeiger nicht verstecken und Tastendrücke wiederholt senden.
    pygame.display.set_caption("ATC-Sim: Test")
    pygame.mouse.set_visible(1)
    pygame.key.set_repeat(1, 30)
 
    # Clock-Objekt erstellen, das wir benötigen, um die Framerate zu begrenzen.
    clock = pygame.time.Clock()
 
 
 
    ###INITIALISING VARIABLES
    # Die Schleife, und damit unser Spiel, läuft solange running == True.
    TIMEREVENT = pygame.USEREVENT
    pygame.time.set_timer(TIMEREVENT, 2000)
    
    running = True
    planes = {}
    deletedPlanes = []
    hilfLabelUpdate = False

    while running:
        # Framerate auf 30 Frames pro Sekunde beschränken.
        # Pygame wartet, falls das Programm schneller läuft.
        clock.tick(30)
 
        # screen-Surface mit weiß füllen.
        screen.fill((255, 255, 255))
 
        # Alle aufgelaufenen Events holen und abarbeiten.
        for event in pygame.event.get():
            # Spiel beenden, wenn wir ein QUIT-Event finden.
            if event.type == pygame.QUIT:
                running = False
 
            if event.type == TIMEREVENT:
                for x in planes:
                    vecs = planes[x].getVector()
                    pos = planes[x].getPosition()
                    if pos[0] < 0 or pos[0] > pygame.display.Info().current_w or pos[1] < 0 or pos[1] > pygame.display.Info().current_h:
                        if x not in deletedPlanes:
                            planes[x].__del__()
                            deletedPlanes.append(x)
                    else:
                        planes[x].update(screen, pos[0]+vecs[0], pos[1]+vecs[1])
                        
                    #allways but only call when screen was updated
                    pygame.display.flip()
 
 
            # Wir interessieren uns auch für "Taste gedrückt"-Events.
            if event.type == pygame.KEYDOWN:
                # Wenn Escape gedrückt wird, posten wir ein QUIT-Event in Pygames Event-Warteschlange.
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                if event.key == pygame.K_DOWN:
                    gen = FlightGenerator().generateFlight()
                    hilf = Tracker.ident #weil sonst init von Tracker hochzählt                    
                    planes[hilf] = Tracker(240, 180, gen[0], gen[1])
                    planes[hilf].setVector(gen[2], gen[3])
                #if event.key == pygame.MOUSEBUTTONDOWN:
            if event.type == pygame.MOUSEBUTTONDOWN:
                klickedX = event.pos[0]
                klickedY = event.pos[1]

                for x in planes:
                    #vecs = planes[x].getVector()
                    pos = planes[x].getPosition()
            
                    #turn label after mouseevent happend AND that within an aircraft
                    if klickedX < pos[0]+5 and klickedX > pos[0]-5 and klickedY < pos[1]+5 and klickedY > pos[1]-5:
                        planes[x].updateLabelPosition()
                
                        #allways but only call when screen was updated
                        pygame.display.flip()
 
# Überprüfen, ob dieses Modul als Programm läuft und nicht in einem anderen Modul importiert wird.
if __name__ == '__main__':
    # Unsere Main-Funktion aufrufen.
    main()