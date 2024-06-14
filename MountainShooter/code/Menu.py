import pygame
from pygame import Rect,Surface
from pygame.font import Font
from code.Const import W_WIDTH

class Menu:
    def __init__(self,window):
        self.window: pygame.Surface = window #Ao inicializar esse objeto, add um parametro window que recebe self.window
        self.surf = pygame.image.load('./asset/MenuBg.png') #self é o que diferencia variavel de atributo
        self.rect = self.surf.get_rect(left = 0,top = 0)


    def run(self, ):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf,dest=self.rect) #Desenhe o self surf no self rect
            self.menu_text(50,"Mountain",(255,128,0),((W_WIDTH/2),70)) #O Self é pra reconhecer que é o metodo da propria classe
            pygame.display.flip() #Atualize a tela  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('loop end')
                    pygame.quit()
                    quit()
    
    def menu_text(self,text_size:int,text:str,text_color: tuple,text_center_pos: tuple): #texto é uma imagem
        text_font: Font = pygame.font.SysFont("Lacida Sans Typewriter",size = text_size)
        text_surf: Surface = text_font.render(text,True,text_color)
        text_react: Rect = text_surf.get_rect(center = text_center_pos)
        self.window.blit(source=text_surf,dest=text_react)



