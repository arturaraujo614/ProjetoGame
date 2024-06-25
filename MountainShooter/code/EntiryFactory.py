import random
from code.Enemy import Enemy
from code.Player import Player
from code.Const import W_HEIGHT, W_WIDTH
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
            case 'Player1':
                return Player('Player1', (10, W_HEIGHT / 2 + 40))
            case 'Player2':
                return Player('Player2', (10, W_HEIGHT / 2 - 40))
            case 'Enemy1':
                return Enemy('Enemy1',(W_WIDTH + 10,random.randint(0 + 40, W_HEIGHT-40)))
            case 'Enemy2':
                return Enemy('Enemy2',(W_WIDTH + 10,random.randint(0 + 40, W_HEIGHT-40)))

