import pygame

#inicia janela
pygame.init()

tela = pygame.display.set_mode((800, 600)) #config da janela
backgroundColor = (255,0, 0) #cor da janela em rgb

run = True
#este while é importante para que a janela não feche automaticamnete, já que se fizer normal SEM O WHILE, A JANLEA IRÁ ABRIR E FECHAR NO INSTANTE.
while  run:
    for evento in pygame.event.get(): #pega vários eventos que correm na janela
        if evento.type ==pygame.QUIT:#se assim que fechar a janela, o run será false e assim termina o loop
            run = False 
        
    tela.fill(backgroundColor) #preenche  a janela com a cor de fundo VERMELHO 

    pygame.display.flip()

pygame.quit()

