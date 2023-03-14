import sys
from typing import Text

import pygame
from pygame.locals import *


def bitfunc (var_a, var_b):
    text1 = bitfont.render(var_a, True, black)
    textrect1 = text1.get_rect()
    textrect1.center = (var_b)
    displaysurf.blit(text1, textrect1)

def answerfunc (var_b2):
    text2 = answerfont.render(str(answer), True, black)
    textrect2 = text2.get_rect()
    textrect2.center = (var_b2)
    displaysurf.blit(text2, textrect2)

def keynumberfunc (var_a3, var_b3):
    text3 = keynumberfont.render(var_a3, True, red)
    textrect3 = text3.get_rect()
    textrect3.center = (var_b3, 240)
    displaysurf.blit(text3, textrect3)

white = (255, 255, 255)
black = (0, 0, 0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

coords0 = (137, 200)
coords1 = (273, 200)
coords2 = (410, 200)
coords3 = (546, 200)
coords4 = (683, 200)
coords5 = (820, 200)
coords6 = (956, 200)
coords7 = (1093, 200)
coords8 = (1229, 200)

answercoords = (683, 384)
answer = 0

tempvar = '0'

bit0 = '0'
bit1 = '0'
bit2 = '0'
bit3 = '0'
bit4 = '0'
bit5 = '0'
bit6 = '0'
bit7 = '0'
bit8 = '0'

zeroispressed = 0

pygame.init()

displaysurf = pygame.display.set_mode((1366, 768))

pygame.display.set_caption('Binärt')

display_width = displaysurf.get_width()
display_height = displaysurf.get_height()

bitfont = pygame.font.Font('freesansbold.ttf', 64)
answerfont = pygame.font.Font('freesansbold.ttf', 128)
keynumberfont = pygame.font.Font('freesansbold.ttf', 32)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_1:
                if bit0 == '0':
                    answer += 1
                bit0 = '1'
            if event.key == pygame.K_2:
                if bit1 == '0':
                    answer += 2
                bit1 = '1'
            if event.key == pygame.K_3:
                if bit2 == '0':
                    answer += 4
                bit2 = '1'
            if event.key == pygame.K_4:
                if bit3 == '0':
                    answer += 8
                bit3 = '1'
            if event.key == pygame.K_5:
                if bit4 == '0':
                    answer += 16
                bit4 = '1'
            if event.key == pygame.K_6:
                if bit5 == '0':
                    answer += 32
                bit5 = '1'
            if event.key == pygame.K_7:
                if bit6 == '0':
                    answer += 64
                bit6 = '1'
            if event.key == pygame.K_8:
                if bit7 == '0':
                    answer += 128
                bit7 = '1'
            if event.key == pygame.K_9:
                if bit8 == '0':
                    answer += 256
                bit8 = '1'
            
            if event.key == pygame.K_r:
                bit0 = '0'
                bit1 = '0'
                bit2 = '0'
                bit3 = '0'
                bit4 = '0'
                bit5 = '0'
                bit6 = '0'
                bit7 = '0'
                bit8 = '0'
                answer = 0

    displaysurf.fill(white)

    bitfunc(bit0, coords0)
    bitfunc(bit1, coords1)
    bitfunc(bit2, coords2)
    bitfunc(bit3, coords3)
    bitfunc(bit4, coords4)
    bitfunc(bit5, coords5)
    bitfunc(bit6, coords6)
    bitfunc(bit7, coords7)
    bitfunc(bit8, coords8)

    keynumberfunc('1', 137)
    keynumberfunc('2', 273)
    keynumberfunc('3', 410)
    keynumberfunc('4', 546)
    keynumberfunc('5', 683)
    keynumberfunc('6', 820)
    keynumberfunc('7', 956)
    keynumberfunc('8', 1093)
    keynumberfunc('9', 1229)

    answerfunc(answercoords)

    pygame.display.update()
    clock.tick(30)