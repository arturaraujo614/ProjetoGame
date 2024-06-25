#!/usr/bin/python
#-*- coding: utf-8 -*-
import random
from pygame import Surface
import pygame
from code.Const import EVENT_ENEMY, MENU_OPTION
from code.Entity import Entity
from code.EntiryFactory import EntiryFactory
from pygame import Rect,Surface
from pygame.font import Font


class Level:
    def __init__(self,window,name,menu_option):
        self.window:Surface = window
        self.name = name
        self.mode = menu_option #Opção do Menu
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntiryFactory.get_entity('Level1Bg')) #O extend irá extender a entity_list para a lista_bg que irá receber
        self.entity_list.append(EntiryFactory.get_entity('Player1')) #Aqui usei o appen pois é apenas 1 entidade, nao uma lista
        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntiryFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY,4000)

    def run(self):
        # pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        # pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(45)
            for ent in self.entity_list:
                self.window.blit(source = ent.surf,dest=ent.rect) #aqui desenho as entidades
                # self.level_text(14, f'fps:{clock.get_fps():.0f}',COLOR_WHITE,(10,10))
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1','Enemy2'))
                    self.entity_list.append(EntiryFactory.get_entity(choice))
            pygame.display.flip()

    def level_text(self,text_size:int,text:str,text_color: tuple,text_pos: tuple): #texto é uma imagem
        text_font: Font = pygame.font.SysFont("Lacida Sans Typewriter",size = text_size)
        text_surf: Surface = text_font.render(text,True,text_color).convert_alpha()
        text_react: Rect = text_surf.get_rect(left = text_pos[0],top=text_pos[1])
        self.window.blit(source=text_surf,dest=text_react)