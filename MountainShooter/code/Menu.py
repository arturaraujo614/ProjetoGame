import pygame
from pygame import Rect,Surface
from pygame.font import Font
from code.Const import COLOR_YELLOW, W_WIDTH,COLOR_ORANGE,MENU_OPTION,COLOR_WHITE

class Menu:
    def __init__(self,window):
        self.window: pygame.Surface = window #Ao inicializar esse objeto, add um parametro window que recebe self.window
        self.surf = pygame.image.load('./asset/MenuBg.png') #self é o que diferencia variavel de atributo
        self.rect = self.surf.get_rect(left = 0,top = 0)


    def run(self, ):
        # pygame.mixer_music.load('./asset/Menu.mp3')
        # pygame.mixer_music.play(-1)
        menu_option = 0
        while True:
            # Desenhar na Tela
            self.window.blit(source=self.surf,dest=self.rect) #Desenhe o self surf no self rect
            self.menu_text(50,"Mountain",COLOR_ORANGE,((W_WIDTH/2),100))#70 #O Self é pra saber que é o metodo da propria classe
            self.menu_text(50,"Shooter",COLOR_ORANGE,((W_WIDTH/2),140)) #110

            for i in range(len(MENU_OPTION)):
                if i ==menu_option:
                    self.menu_text(25,MENU_OPTION[i],COLOR_YELLOW,((W_WIDTH/2),200+20*i))
                else: self.menu_text(25,MENU_OPTION[i],COLOR_WHITE,((W_WIDTH/2),200+20*i))
            pygame.display.flip() #Atualize a tela

            # Verificar Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) -1:
                            menu_option +=1 
                        else: menu_option = 0 
                    
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -=1 
                        else: menu_option = len(MENU_OPTION) -1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]
    
    def menu_text(self,text_size:int,text:str,text_color: tuple,text_center_pos: tuple): #texto é uma imagem
        text_font: Font = pygame.font.SysFont("Lacida Sans Typewriter",size = text_size)
        text_surf: Surface = text_font.render(text,True,text_color).convert_alpha()
        text_react: Rect = text_surf.get_rect(center = text_center_pos)
        self.window.blit(source=text_surf,dest=text_react)



