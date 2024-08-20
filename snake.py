import pygame
from pygame.locals import *
import random

dificuldade = 2
tamanhoMaximo = 800
width = tamanhoMaximo
height = tamanhoMaximo
widthPt = 20*dificuldade
heightPt = 20*dificuldade
pixelRadius  = width//widthPt
print(pixelRadius)
tamanhoFonte = 24
tamanhoFonte2 = 16
dimensoes = (width,height)
corFundo = (255,255,255)
corSnake = (0,0,0)
corFruta = (255,0,0)
speed = int(5+7*dificuldade)

statusGame = 1

def eat(p1, p2):
    return (p1[0]==p2[0]) and (p1[1]==p2[1])
def collision(p1,limites):
    return not(0<=p1[0]<=limites[0]) or not(0<=p1[1]<=limites[1])
def initGame(n=3):
    global snake, apple_pos, statusGame
    meiaAltura = heightPt//2*pixelRadius
    meiaLargura = widthPt//2*pixelRadius
    snake = []
    for i in range(n):
        snake.append((meiaLargura-i*pixelRadius,meiaAltura))
    apple_pos = (random.randrange(0,width-pixelRadius,pixelRadius),random.randrange(0,height-pixelRadius,pixelRadius))
    statusGame = 1

pygame.init()
screen = pygame.display.set_mode(dimensoes)
pygame.display.set_caption("Snake")

UP = +1
RIGHT = +2
DOWN = -1
LEFT = -2

initGame(5)
print(snake)
# SNAKE
snake_skin = pygame.Surface((pixelRadius,pixelRadius))
snake_skin.fill(corSnake)
myDirection = RIGHT

# APPLE
apple = pygame.Surface((pixelRadius,pixelRadius))
apple.fill(corFruta)

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', tamanhoFonte)
text = font.render("GAME OVER",True,corSnake)
textRect = text.get_rect()
textRect.center = (width//2,height//2-tamanhoFonte)

font2 = pygame.font.Font('freesansbold.ttf', tamanhoFonte2)
text2 = font2.render("Aperte ENTER para reiniciar.",True,corSnake)
textRect2 = text2.get_rect()
textRect2.center = (width//2,height//2+tamanhoFonte2)

while True:
    clock.tick(speed)
    print(snake)
    hungerSnake = True
    for event in pygame.event.get():
        
        # Controles Off Game:
        if event.type == QUIT:
            pygame.quit()

        # Controles In Game:
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
            if statusGame==1:
                if event.key == K_UP and (myDirection + UP != 0):
                    myDirection = UP
                if event.key == K_DOWN and (myDirection + DOWN != 0):
                    myDirection = DOWN
                if event.key == K_LEFT and (myDirection + LEFT != 0):
                    myDirection = LEFT
                if event.key == K_RIGHT and (myDirection + RIGHT != 0):
                    myDirection = RIGHT
            elif statusGame==0:
                if event.key == pygame.K_RETURN:
                    initGame()
    
    # Verificações e Atualizações In Game
    if statusGame==1:
        if eat(apple_pos,snake[0]):
            while (apple_pos in snake):
                apple_pos = (random.randrange(0,width-pixelRadius,pixelRadius),random.randrange(0,height-pixelRadius,pixelRadius))            
            hungerSnake = False
        if collision(snake[0],dimensoes):
            statusGame = 0
        if myDirection == UP:
            snake[0:0] = [(snake[0][0],snake[0][1] - pixelRadius)]
        if myDirection == DOWN:
            snake[0:0] = [(snake[0][0],snake[0][1] + pixelRadius)]
        if myDirection == LEFT:
            snake[0:0] = [(snake[0][0] - pixelRadius,snake[0][1])]
        if myDirection == RIGHT:
            snake[0:0] = [(snake[0][0] + pixelRadius,snake[0][1])]
        
        if hungerSnake:
            del snake[-1]

    # Renderizar a tela
    screen.fill(corFundo)
    screen.blit(apple,apple_pos)
    for pos in snake:
        screen.blit(snake_skin,pos)
    
    if statusGame == 0:
        screen.blit(text,textRect)
        screen.blit(text2,textRect2)
    
    pygame.display.update()