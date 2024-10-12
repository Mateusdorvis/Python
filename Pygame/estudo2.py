import pygame
#SIMULADOR DE POSIÇÃO DE FIGURAS NO PYGAME, ESTA FERRAMENTA VAI AJUDAR MELHOR NA POSIÇÃO DAS FIGURAS
#inicia janela
pygame.init()

tela = pygame.display.set_mode((800, 600)) #config da janela
backgroundColor = (255,0, 0) #cor da janela em rgb

corquadrado = (255, 255,0)
eixo_x = 0 #posição inicial
eixo_y = 0 #posição inicial
altura_quadrado = 200
largura_quadrado = 200

fonte = pygame.font.Font(None, 18)
velocidade = 5
run = True
texto_quadrado = ''

#este while é importante para que a janela não feche automaticamnete, já que se fizer normal SEM O WHILE, A JANLEA IRÁ ABRIR E FECHAR NO INSTANTE.
while  run:
    for evento in pygame.event.get(): #pega vários eventos que correm na janela
        if evento.type ==pygame.QUIT:#se assim que fechar a janela, o run será false e assim termina o loop
            run = False 
    tecla_pressionada = pygame.key.get_pressed()

    if tecla_pressionada[pygame.K_LEFT]:
        eixo_x -= velocidade
        
    
    if tecla_pressionada[pygame.K_DOWN]:
        eixo_y += velocidade
        
    
    if tecla_pressionada[pygame.K_UP]:
        eixo_y -= velocidade
        
    
    if tecla_pressionada[pygame.K_RIGHT]:
        eixo_x += velocidade
       

    eixo_x = max(0, min(eixo_x, 800 - largura_quadrado))
    eixo_y  = max(0, min(eixo_y, 600 - altura_quadrado))

    texto_quadrado = f'''Posição ({eixo_x}  d r, {eixo_y} d t)'''

    tela.fill(backgroundColor) #preenche  a janela com a cor de fundo VERMELHO 
    pygame.draw.rect(tela, corquadrado, (eixo_x, eixo_y, largura_quadrado, altura_quadrado))#desenhando um quadrado na tela

    texto_redenrizado = fonte.render(texto_quadrado, True, (0,0,0))#redenriza um texto na tela

    tela_rect = texto_redenrizado.get_rect(center=(eixo_x+largura_quadrado//2, eixo_y+altura_quadrado//2))
    
    tela.blit(texto_redenrizado, tela_rect)

    pygame.display.flip()
    

pygame.quit()

