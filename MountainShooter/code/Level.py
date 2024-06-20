#!/usr/bin/python
#-*- coding: utf-8 -*-
from pygame import Surface
import pygame
from code.Entity import Entity
from code.EntiryFactory import EntiryFactory


class Level:
    def __init__(self,window,name,menu_option):
        self.window:Surface = window
        self.name = name
        self.mode = menu_option #Opção do Menu
        self.entiry_list: list[Entity] = []
        self.entiry_list.extend(EntiryFactory.get_entity('Level1Bg',(0,0))) #O extend irá extender a entiry_list para a lista_bg que irá receber


    def run(self, ):
        while True:
            for ent in self.entiry_list:
                self.window.blit(source = ent.surf,dest=ent.rect)
                ent.move()
            pygame.display.flip()

