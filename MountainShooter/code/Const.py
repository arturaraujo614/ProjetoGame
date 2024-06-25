#W
import pygame


W_WIDTH = 576
W_HEIGHT = 324

#C
COLOR_ORANGE = (255,128,0)
COLOR_WHITE = (255,255,255)
COLOR_YELLOW = (255,255,128)
COLOR_GREEN = (110,177,58)

#M
MENU_OPTION = ('NEW GAME 1P',
               'NEM GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'EXIT')

#E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {'Level1Bg0':4,
                'Level1Bg1':5,
                'Level1Bg2':6,
                'Level1Bg3':6,
                'Level1Bg4':7,
                'Level1Bg5':8,
                'Level1Bg6':8,
                'Level1Bg7':9,
                'Player1':4,
                'Player2':4,
                'Enemy1':3,
                'Enemy2':4
                }

PLAYER_KEY_UP = {'Player1':pygame.K_UP,
                 'Player2':pygame.K_w}
PLAYER_KEY_DOWN = {'Player1':pygame.K_DOWN,
                 'Player2':pygame.K_s}
PLAYER_KEY_LEFT = {'Player1':pygame.K_LEFT,
                 'Player2':pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1':pygame.K_RIGHT,
                 'Player2':pygame.K_d}