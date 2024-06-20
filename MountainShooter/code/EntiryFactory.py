#!/usr/bin/python
#-*- coding: utf-8 -*-
from code.Const import W_WIDTH
from code.Background import Background

class EntiryFactory:
    @staticmethod
    def get_entity(entity_name:str,position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                lista_bg = []
                for i in range(7):
                    lista_bg.append(Background(f'Level1Bg{i}',(0,0)))
                    lista_bg.append(Background(f'Level1Bg{i}',(W_WIDTH,0)))
                return lista_bg

