import pygame

#inicia janela
pygame.init()

tela = pygame.display.set_mode((800, 600)) #config da janela


imagem  = pygame.image.load(r'C:\xampp\htdocs\progr\python\ARTE\skylite\oi.jpg') #carrrando uma imaem

image_positionx = 0
image_positiony = 0


eixo_x = 0
eixo_y = 0
velocidade = 5
run = True

#este while é importante para que a janela não feche automaticamnete, já que se fizer normal SEM O WHILE, A JANLEA IRÁ ABRIR E FECHAR NO INSTANTE.
while  run:
    for evento in pygame.event.get(): #pega vários eventos que correm na janela
        if evento.type ==pygame.QUIT:#se assim que fechar a janela, o run será false e assim termina o loop
            run = False 
        tecla_pressionada = pygame.key.get_pressed()

    if tecla_pressionada[pygame.K_LEFT]:
        eixo_x -= velocidade
     
    
    elif tecla_pressionada[pygame.K_DOWN]:
        eixo_y += velocidade
       
        
   
    
    elif tecla_pressionada[pygame.K_UP]:
        eixo_y -= velocidade
      
     
        
    
    elif tecla_pressionada[pygame.K_RIGHT]:
        eixo_x += velocidade
      
    
   
       

    

    tela.blit(imagem, (image_positionx, image_positiony)) #colocando a imagem dentro da janela e com coordenada
    pygame.draw.rect(tela, (255, 255, 0), (eixo_x, eixo_y, 200, 200))
    pygame.display.flip()

pygame.quit()

