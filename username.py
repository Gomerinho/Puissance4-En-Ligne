#!/usr/bin/python3
import os

import pygame_textinput
import pygame

pygame.init()

# Create TextInput-object
textinput = pygame_textinput.TextInput()

screen = pygame.display.set_mode((1000, 200))
clock = pygame.time.Clock()
j1=''

while True:
    screen.fill((225, 225, 225))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    # Feed it with events every frame
    if textinput.update(events):
        j1 = textinput.get_text()
        print(j1)
        os.system('python game.py')
        exit()

    # Blit its surface onto the screen
    screen.blit(textinput.get_surface(), (10, 10))

    pygame.display.update()
    clock.tick(30)