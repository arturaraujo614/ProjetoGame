
import pygame
from code.Level import Level
from code.Menu import Menu
from code.Const import MENU_OPTION, W_HEIGHT, W_WIDTH

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(W_WIDTH,W_HEIGHT))

    def run(self, ):
        while True:
            menu = Menu(self.window)  # Instancia o Objeto Menu com o parametro de window
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0],MENU_OPTION[1],MENU_OPTION[2]]:
                level = Level(self.window,"Level1",menu_return)
                level_return = level.run()
            else:
                pygame.quit()
                quit()
    
    

