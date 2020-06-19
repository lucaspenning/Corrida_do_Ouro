import pygame
# Funcionalidades do Sistema
import os
import random
# Cores
BLACK = pygame.Color(0, 0, 0)
RED = pygame.Color(255, 0, 0)
BLUE = pygame.Color(0, 0, 255)
GREEN = pygame.Color(0, 255, 0)
WHITE = pygame.Color(255, 255, 255)

pygame.init()

screen = pygame.display.set_mode((1300, 720))

pygame.display.set_caption('Corrida do Ouro')

# Carregando Imagem Moeda
moeda = pygame.image.load(os.path.join('imagens', 'moeda.jpg'))
moeda = moeda.convert_alpha()
# Carregando Imagem Avatar
image = pygame.image.load(os.path.join('imagens', 'avatar.png'))
image = image.convert_alpha()
# Carregando Imagem Cogumelo
cogumelo = pygame.image.load(os.path.join('imagens', 'vida.png'))
cogumelo = cogumelo.convert_alpha()
# Carregando Imagem Canhão
canhao = pygame.image.load(os.path.join('imagens', 'canhao.png'))
canhao = canhao.convert_alpha()
# Carregando Imagem Bala
bala = pygame.image.load(os.path.join('imagens', 'bala.jfif'))
bala_1 = bala.convert_alpha()
bala_2 = bala.convert_alpha()
bala_3 = bala.convert_alpha()
bala_4 = bala.convert_alpha()
bala_5 = bala.convert_alpha()

#Variaveis
start = 0
bola = 0
colisao = 0
pontos = 0
vida = 1

#Posição iniciaç do Avatar
x = 210
y = 210

# cria bala de canhão
square1 = pygame.Rect(500, 230, 30, 30)
square2 = pygame.Rect(500, 230, 30, 30)
square3 = pygame.Rect(500, 230, 30, 30)
square4 = pygame.Rect(500, 230, 30, 30)
square5 = pygame.Rect(500, 230, 30, 30)

# Criar as paredes
up_pad = pygame.Rect(5, 5, 1280, 20)
down_pad = pygame.Rect(5, 700, 1295, 20)
left_pad = pygame.Rect(5, 5, 20, 700)
right_pad = pygame.Rect(1280, 5, 20, 700)
pads_laterais = [left_pad, right_pad]
pads_cima = [up_pad]
pads_baixo = [down_pad]

#Bala 1
bola1_x = 1180
bola1_y = 580
bola1_horizontal = 0
bola1_vertical = 0

#Bala 2
bola2_x = 30
bola2_y = 60
bola2_horizontal = 0
bola2_vertical = 0

#Bala 3
bola3_x = 1180
bola3_y = 580
bola3_horizontal = 0
bola3_vertical = 0

#Bala 4
bola4_x = 30
bola4_y = 60
bola4_horizontal = 0
bola4_vertical = 0

#Bala 5
bola5_x = 1180
bola5_y = 580
bola5_horizontal = 0
bola5_vertical = 0

#Posição moeda
moeda_x = 1000
moeda_y = 1000

#Posição vida
vida_x = 1000
vida_y = 1000

clock = pygame.time.Clock()

#Texto na tela
txt='Pressione S para CONTINUAR'                                 
pygame.font.init()                                
fonte=pygame.font.get_default_font()  
tamanhoFonte = 60       
psx = 400
psy= 300     
fontesys=pygame.font.SysFont(fonte, tamanhoFonte)           
txttela = fontesys.render(txt, 2, BLUE)       
screen.blit(txttela, (psx, psy))    
tempo_clock = 30          

#Loop
while True:
    dt = clock.tick(tempo_clock)

    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        break

    screen.fill(WHITE)
    
    #Verifica se a tecla do pressionada
    keys = pygame.key.get_pressed()
    #Verifica qual tecla foi pressionada
    #Esquerda
    if keys[pygame.K_LEFT]:
        if(x > 30):
            x -= 5
    #Direita
    if keys[pygame.K_RIGHT]:
        if(x < 1180):
            x += 5
    #Cima
    if keys[pygame.K_UP]:
        if(y > 30):
            y -= 5
    #Baixo
    if keys[pygame.K_DOWN]:
        if(y < 600):
            y += 5
    #Introdução
    if keys[pygame.K_s]:
        psx = 100
        psy= 300   
        txt='COLETE 50 MOEDAS PARA GANHAR, P PARA INICIAR'
        txttela = fontesys.render(txt, 2, RED)
    #Posiciona inicialmente Moeda e Vida
    if keys[pygame.K_p]:
        start = 1
        moeda_x =  random.randrange(5,1120)
        moeda_y = random.randrange(5,530)
        vida_x =  random.randrange(5,1120)
        vida_y = random.randrange(5,530)
    #Inicia o Jogo dando valores a variaveis
    if keys[pygame.K_r]:
        start = 1
        pontos = 0
        tempo_clock = 30
        vida =1
        #posição aleatória moeda
        moeda_x =  random.randrange(5,1120)
        moeda_y = random.randrange(5,530)
        #posição aleatória vida
        vida_x =  random.randrange(5,1120)
        vida_y = random.randrange(5,530)
        x = 210
        y = 210
        #Posição de tiro inicial 
        #Bala 1
        bola1_x = 1180
        bola1_y = 580
        bola1_horizontal = 0
        bola1_vertical = 0

        #Bala 2
        bola2_x = 15
        bola2_y = 15
        bola2_horizontal = 0
        bola2_vertical = 0

        #Bala 3
        bola3_x = 1180
        bola3_y = 580
        bola3_horizontal = 0
        bola3_vertical = 0

        #Bala 4
        bola4_x = 15
        bola4_y = 15
        bola4_horizontal = 0
        bola4_vertical = 0

        #Bala 5
        bola5_x = 1180
        bola5_y = 580
        bola5_horizontal = 0
        bola5_vertical = 0

    #Começa
    if(start > 0):
        #Posicionando e jogando imagens dos personagens na tela além de pontuação
        psx = 750
        psy = 25
        tamanhoFonte = 40
        txt='VIDA = ' + str(vida) + '     PONTOS = ' + str(pontos) 
        txttela = fontesys.render(txt, 2, BLACK)
        #Imagem MARIO
        nova_image = pygame.transform.scale(image,(100, 100))
        screen.blit(nova_image, (x, y))    
        #Imagem MOEDA
        nova_moeda = pygame.transform.scale(moeda,(50, 50))
        screen.blit(nova_moeda, (moeda_x, moeda_y))
        #Imagem COGUMELO(VIDA)
        nova_vida = pygame.transform.scale(cogumelo,(50, 50))
        screen.blit(nova_vida, (vida_x, vida_y))
        #Movimentar as balas de canhão de 1 a 5 mesclando movimento horinzontais com verticais, definindo quando cada bala é lançada no mapa
        if(pontos >= 1 ):
            nova_bala_1 = pygame.transform.scale(bala_1,(100, 100))
            screen.blit(nova_bala_1, (bola1_x, bola1_y))
            #Eixo x
            if(bola1_x >= 15 and bola1_horizontal == 0):
                bola1_x += 5;
            if(bola1_x <= 1220 and bola1_horizontal == 1):
                bola1_x -= 5;
            if(bola1_x == 15):
                bola1_horizontal = 0;
                bola1_y -= 5;
                bala_1 = pygame.transform.rotate(bala, 180)
            if(bola1_x == 1220):
                bola1_horizontal = 1;
                bola1_y += 5;
                bala_1 = pygame.transform.rotate(bala, 0)
            #Eixo y
            if(bola1_y >= 15 and bola1_vertical == 0):
                bola1_y += 5;
            if(bola1_y <= 630 and bola1_vertical == 1):
                bola1_y -= 5;
            if(bola1_y == 15):
                bola1_vertical = 0;
                bola1_x -= 5;
            if(bola1_y == 630):
                bola1_vertical = 1;
                bola1_x += 5;
        if(pontos >= 5):
            nova_bala_2 = pygame.transform.scale(bala_2,(100, 100))
            screen.blit(nova_bala_2, (bola2_x, bola2_y))
            #Eixo x
            if(bola2_x >= 15 and bola2_horizontal == 0):
                bola2_x += 5;
            if(bola2_x <= 1220 and bola2_horizontal == 1):
                bola2_x -= 5;
            if(bola2_x == 15):
                bola2_horizontal = 0;
                bola2_y -= 5;
                bala_2 = pygame.transform.rotate(bala, 180)
            if(bola2_x == 1220):
                bola2_horizontal = 1;
                bola2_y += 5;
                bala_2 = pygame.transform.rotate(bala, 0)
            #Eixo y
            if(bola2_y >= 15 and bola2_vertical == 0):
                bola2_y += 5;
            if(bola2_y <= 630 and bola2_vertical == 1):
                bola2_y -= 5;
            if(bola2_y == 15):
                bola2_vertical = 0;
                bola2_x -= 5;
            if(bola2_y == 630):
                bola2_vertical = 1;
                bola2_x += 5;
        if(pontos >= 10):
            nova_bala_3 = pygame.transform.scale(bala_3,(100, 100))
            screen.blit(nova_bala_3, (bola3_x, bola3_y))
            #Eixo x
            if(bola3_x >= 15 and bola3_horizontal == 0):
                bola3_x += 5;
            if(bola3_x <= 1220 and bola3_horizontal == 1):
                bola3_x -= 5;
            if(bola3_x == 15):
                bola3_horizontal = 0;
                bola3_y -= 5;
                bala_3 = pygame.transform.rotate(bala, 180)
            if(bola3_x == 1220):
                bola3_horizontal = 1;
                bola3_y += 5;
                bala_3 = pygame.transform.rotate(bala, 0)
            #Eixo y
            if(bola3_y >= 15 and bola3_vertical == 0):
                bola3_y += 5;
            if(bola3_y <= 630 and bola3_vertical == 1):
                bola3_y -= 5;
            if(bola3_y == 15):
                bola3_vertical = 0;
                bola3_x -= 5;
            if(bola3_y == 630):
                bola3_vertical = 1;
                bola3_x += 5;
        if(pontos >= 18):
            nova_bala_4 = pygame.transform.scale(bala_4,(100, 100))
            screen.blit(nova_bala_4, (bola4_x, bola4_y))
            #Eixo x
            if(bola4_x >= 15 and bola4_horizontal == 0):
                bola4_x += 5;
            if(bola4_x <= 1220 and bola4_horizontal == 1):
                bola4_x -= 5;
            if(bola4_x == 15):
                bola4_horizontal = 0;
                bola4_y -= 5;
                bala_4 = pygame.transform.rotate(bala, 180)
            if(bola4_x == 1220):
                bola4_horizontal = 1;
                bola4_y += 5;
                bala_4 = pygame.transform.rotate(bala, 0)
            #Eixo y
            if(bola4_y >= 15 and bola4_vertical == 0):
                bola4_y += 5;
            if(bola4_y <= 630 and bola4_vertical == 1):
                bola4_y -= 5;
            if(bola4_y == 15):
                bola4_vertical = 0;
                bola4_x -= 5;
            if(bola4_y == 630):
                bola4_vertical = 1;
                bola4_x += 5;
        if(pontos >= 25):
            nova_bala_5 = pygame.transform.scale(bala_5,(100, 100))
            screen.blit(nova_bala_5, (bola5_x, bola5_y))
            #Eixo x
            if(bola5_x >= 15 and bola5_horizontal == 0):
                bola5_x += 5;
            if(bola5_x <= 1220 and bola5_horizontal == 1):
                bola5_x -= 5;
            if(bola5_x == 15):
                bola5_horizontal = 0;
                bola5_y -= 5;
                bala_5 = pygame.transform.rotate(bala, 180)
            if(bola5_x == 1220):
                bola5_horizontal = 1;
                bola5_y += 5;
                bala_5 = pygame.transform.rotate(bala, 0)
            #Eixo y
            if(bola5_y >= 15 and bola5_vertical == 0):
                bola5_y += 5;
            if(bola5_y <= 630 and bola5_vertical == 1):
                bola5_y -= 5;
            if(bola5_y == 15):
                bola5_vertical = 0;
                bola5_x -= 5;
            if(bola5_y == 630):
                bola5_vertical = 1;
                bola5_x += 5;
    
    #Figura canhão e Texto
    screen.blit(txttela,(psx, psy))
    novo_canhao = pygame.transform.scale(canhao,(100, 100))
    screen.blit(novo_canhao, (15, 15))
    canhao_2 = pygame.transform.rotate(canhao, 180)
    novo_canhao_2 = pygame.transform.scale(canhao_2,(100, 100))
    screen.blit(novo_canhao_2, (1180, 600))

    #Verificando colisão das balas com o avatar
    if(((x >= bola1_x-80) & (x <= bola1_x+80))  &  ((y >= bola1_y-80) &- (y <= bola1_y+80)) and pontos > 0):
        vida -= 1 
        bola1_x = 30
        bola1_y = 60
    if(((x >= bola2_x-80) & (x <= bola2_x+80))  &  ((y >= bola2_y-80) & (y <= bola2_y+80)) and pontos > 4):
        vida -= 1
        bola2_x = 1180
        bola2_y = 580
    if(((x >= bola3_x-80) & (x <= bola3_x+80))  &  ((y >= bola3_y-80) & (y <= bola3_y+80)) and pontos > 9):
        vida -= 1
        bola3_x = 30
        bola3_y = 60
    if(((x >= bola4_x-80) & (x <= bola4_x+80))  &  ((y >= bola4_y-80) & (y <= bola4_y+80)) and pontos > 17):
        vida -= 1
        bola4_x = 1180
        bola4_y = 580
    if(((x >= bola5_x-80) & (x <= bola5_x+80))  &  ((y >= bola5_y-80) & (y <= bola5_y+80)) and pontos > 24):
        vida -= 1
        bola4_x = 30
        bola4_y = 60
        
    #Verificando sem o avatar está com vida
    if(vida == 0):
        start = 0
        psx = 50
        psy = 200
        txt='FALECEU COM ' + str(pontos) + ' PONTOS, R PARA RECOMEÇAR O JOGO'
        txttela = fontesys.render(txt, 2, RED)
        
    #Virifcando pontuação para vitória
    if(pontos == 50):
        start = 0
        psx = 50
        psy = 200
        txt='VOCÊ GANHOU! PRESSIONE R PARA REINICIAR' 
        txttela = fontesys.render(txt, 2, GREEN)
    
    #Verifica colisão do avatar com a moeda para coleta além de distribuir vidas entre determinadas pontuações
    if(((x >= moeda_x-100) & (x <= moeda_x+100))  &  ((y >= moeda_y-100) & (y <= moeda_y+100))):
        pontos += 1
        temp = 0
        #posição aleatória
        moeda_x =  random.randrange(5,1180)
        moeda_y = random.randrange(5,530)
        #Vidas aleatórias no mapa e aumentando velocidade do jogo conforme pontuação
        if(pontos == 2 ):
            vida_x =  random.randrange(5,1180)
            vida_y = random.randrange(5,530) 
            tempo_clock = 35
        if(pontos == 7):
            vida_x =  random.randrange(5,1180)
            vida_y = random.randrange(5,530) 
            tempo_clock = 40   
        if(pontos == 10):
            vida_x =  random.randrange(5,1180)
            vida_y = random.randrange(5,530)  
            tempo_clock = 47 
        if(pontos == 18):
            vida_x =  random.randrange(5,1180)
            vida_y = random.randrange(5,530) 
            tempo_clock = 55  
        if(pontos == 20):
            vida_x =  random.randrange(5,1180)
            vida_y = random.randrange(5,530)  
            tempo_clock = 63
        if(pontos == 25):
            vida_x =  random.randrange(5,1180)
            vida_y = random.randrange(5,530)   
            tempo_clock = 70
        if(pontos == 34):
            vida_x =  random.randrange(5,1180)
            vida_y = random.randrange(5,530)
            tempo_clock = 80
    
    #Verifica colisão do avatar com a vida para a coleta    
    if(((x >= vida_x-100) & (x <= vida_x+100))  &  ((y >= vida_y-100) & (y <= vida_y+100))):
        vida += 1
        #tira vida do alcance do avatar
        vida_x = 1500
        vida_y = 1500

    # desenha as paredes
    for pad in pads_cima:
        pygame.draw.rect(screen, RED, pad)
    for pad in pads_baixo:
        pygame.draw.rect(screen, RED, pad)
    for pad in pads_laterais:
        pygame.draw.rect(screen, RED, pad)

    pygame.display.flip()