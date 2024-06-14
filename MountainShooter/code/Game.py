
import pygame

from code.Menu import Menu
from code.Const import W_HEIGHT, W_WIDTH

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(W_WIDTH,W_HEIGHT))

    def run(self, ):
        while True:
            menu = Menu(self.window)  # Instancia o Objeto Menu com o parametro de window
            menu.run()
    
    

