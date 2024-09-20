
import pygame

pygame.init()

janela = pygame.display.set_mode([1000, 750])
pygame.display.set_caption('Ping Pong')

BRANCO = (80,80,80)
PRETO = ("#229A00")

raquete1_x, raquete1_y = 20, 375
raquete2_x, raquete2_y = 970, 375
bola_x, bola_y = 500, 375


velocidade_raquete = 1.5
velocidade_bola_x, velocidade_bola_y = 0.5, 0.75



raquete_largura, raquete_altura = 20, 100
bola_largura, bola_altura = 20, 20


placar1 = 0
placar2 = 0
font = pygame.font.SysFont(None, 55)
pontuacao_placar2 = '0'
# Função para desenhar elementos
def desenhar():
    # Limpa a tela
    janela.fill(BRANCO)
    
    
    pygame.draw.rect(janela, PRETO, (raquete1_x, raquete1_y, raquete_largura, raquete_altura))
    pygame.draw.rect(janela, PRETO, (raquete2_x, raquete2_y, raquete_largura, raquete_altura))
    pygame.draw.ellipse(janela, (255,255,255), (bola_x, bola_y, bola_largura, bola_altura))
    
    pygame.draw.rect(janela,"#FF6400",(335,43,200,50))

    placar_texto = font.render(f'{placar1} - {placar2}', True, (0,0,0))
    pontuacao_placar2 = font.render(f'Jogardor 2 marcou ponto',True,(255,255,255))
    janela.blit(placar_texto, (400, 50))
    return pontuacao_placar2


LOOP = True

while LOOP:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            LOOP = False

    # Movimentação das raquetes
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and raquete1_y > 0:
        raquete1_y -= velocidade_raquete
    if keys[pygame.K_s] and raquete1_y < 750 - raquete_altura:
        raquete1_y += velocidade_raquete
    if keys[pygame.K_UP] and raquete2_y > 0:
        raquete2_y -= velocidade_raquete
    if keys[pygame.K_DOWN] and raquete2_y < 750 - raquete_altura:
        raquete2_y += velocidade_raquete
    
    bola_x += velocidade_bola_x
    bola_y += velocidade_bola_y

    if bola_y <= 0 or bola_y > 750 - bola_altura:
        velocidade_bola_y = -velocidade_bola_y
    if bola_x <= 0 or bola_x > 1000 - bola_altura:
        velocidade_bola_x = -velocidade_bola_x
    
    if (raquete1_x<bola_x<raquete1_x + raquete_largura) and (raquete1_y < bola_y<raquete1_y + raquete_altura):
        velocidade_bola_x = - velocidade_bola_x

    if (raquete2_x<bola_x<raquete2_x + raquete_largura) and (raquete2_y < bola_y< raquete2_y + raquete_altura):
        velocidade_bola_x = - velocidade_bola_x

    

    if bola_x == 0:
        
        janela.blit(pontuacao_placar2, (500,375))
        placar2 += 1
        velocidade_bola_x = -velocidade_bola_x
        bola_x, bola_y = 500,375
        
    if bola_x >= 1000 - raquete_largura :
        placar1 += 1
        velocidade_bola_x = -velocidade_bola_x
        bola_x, bola_y = 500,375
    




    desenhar()
    pygame.display.update()



