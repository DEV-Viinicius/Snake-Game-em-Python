import pygame
from pygame.locals import*
from sys import exit
from random import randint

pygame.init()
Pontos = 0
fonte = pygame.font.SysFont('Arial',20,True,False)
largura =640
altura =480 
relogio = pygame.time.Clock()
x = 320
y = 240

x_comida= 300
y_comida= 200


x_cobra = 20
y_cobra = 20


velocidade = 10
x_controle = velocidade
y_controle =0


tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('jogo_da_cobra')
cor = (255,255,255)
tela.fill(cor)
pygame.display.flip()
lista_cobra = []


comprimento_inicial = 5
morreu = False


def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela,(0,255,0),(XeY[0],XeY[1],20,20))

def reiniciar_jogo():
    global Pontos,comprimento_inicial,x_cobra,y_cobra,lista_cobra,lista_cabeca,x_comida,y_comida,morreu
    Pontos=0
    comprimento_inicial=5
    x_cobra = 20
    y_cobra = 20
    lista_cobra=[]
    lista_cabeca=[]
    x_comida= randint (40,630)
    y_comida = randint(50,430)
    morreu=False


    
 

while True: 
    relogio.tick(20)
    tela.fill(cor)
    mesagem= f'Pontos:{Pontos}'
    texto_formatado = fonte.render(mesagem,True,(0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit
            exit()

    if event.type == KEYDOWN:
        if event.key == K_DOWN:
            if y_controle == -velocidade:
                pass
            else:
                y_controle = velocidade
                x_controle = 0
        if event.key == K_UP:
            if y_controle == velocidade :
                pass
            else:
                y_controle = -velocidade
                x_controle = 0
        if event.key == K_LEFT:
            if x_controle == velocidade:
                pass
            else:
                x_controle = -velocidade 
                y_controle = 0
        if event.key == K_RIGHT:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0

    x_cobra=x_cobra+x_controle
    y_cobra = y_cobra+ y_controle

    cobra = pygame.draw.rect(tela,(0,255,0),(x_cobra,y_cobra,20,20)) 
    comida = pygame.draw.rect(tela,(255,0,0),(x_comida,y_comida,20,20))

    if cobra.colliderect(comida):
        x_comida= randint (40,630)
        y_comida = randint(50,430)
        Pontos=Pontos+1
        comprimento_inicial=comprimento_inicial+1

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1 :
        fonte2=pygame.font.SysFont('arail',20,True,True)
        mesagem= 'GAME OVER! Pressione a tecla R para jogar novamente '
        texto_formatado=fonte2.render(mesagem, True,(255,0,0))
        ret_texto = texto_formatado.get_rect()
        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type== KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            ret_texto.center=largura//2,altura//2
            tela.blit(texto_formatado,(ret_texto))
            pygame.display.update()

    if x_cobra >largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0



    if len (lista_cobra)>comprimento_inicial:
        del lista_cobra[0]


    aumenta_cobra(lista_cobra)


    tela.blit(texto_formatado,(530,0))
    pygame.display.update()