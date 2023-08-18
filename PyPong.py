import pygame
import random

pygame.init()
clock = pygame.time.Clock()

screenWidth = 1280
screenHeight = 960

screen = pygame.display.set_mode ((screenWidth, screenHeight))

pygame.display.set_caption ("PyPong!")

font = pygame.font.Font('freesansbold.ttf',32)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

playerScoreX = screenWidth - (screenWidth / 3)
playerScoreY = 10

opponentScoreX = screenWidth / 5
opponentScoreY = 10

ball = pygame.Rect(screenWidth/2 - 15, screenHeight/2 - 15, 30, 30)
player = pygame.Rect (screenWidth - 20, screenHeight/2-70, 10, 140)
opponent = pygame.Rect (10, screenHeight/2-70, 10, 140)

bgColour = pygame.Color("grey12")
lightGrey = (200,200,200)

ballSpeedX = 7 * random.choice((1,-1))
ballSpeedY = 7 * random.choice((1,-1))
playerYSpeed = 0
opponentSpeed = 7
playerScore = 0
opponentScore = 0

def showScore(x,y, ox, oy):
    global playerScore, opponentScore

    scoreImg = font.render("Score : " + str(playerScore), True, (255,255,255))
    rect = scoreImg.get_rect()
    pygame.draw.rect(scoreImg, GREEN, rect, 1)

    screen.blit(scoreImg, (x,y))

    scoreImg = font.render("Score : " + str(opponentScore), True, (255,255,255))
    rect = scoreImg.get_rect()
    pygame.draw.rect(scoreImg, GREEN, rect, 1)

    screen.blit(scoreImg, (ox,oy))

    #opponentScore = font.render("Score : " + str(opponentScore), True, (255,255,255))
    #screen.blit(opponentScore, (ox,oy))

def moveBall():
    global ballSpeedX, ballSpeedY, playerScore, opponentScore
    ball.x += ballSpeedX
    ball.y += ballSpeedY

    if ball.top <= 0 or ball.bottom >= screenHeight:
        ballSpeedY *= -1

    if ball.left <= 0:
        playerScore += 1
        ballRestart()
    if ball.right >= screenWidth:
        ballRestart()
        opponentScore += 1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ballSpeedX *= -1

def playerAnimation():
    player.y += playerYSpeed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screenHeight:
        player.bottom = screenHeight

def opponentAnimation():
    if opponent.top < ball.y:
        opponent.top += opponentSpeed
    if opponent.top > ball.y:
        opponent.top -= opponentSpeed

def ballRestart():
    global ballSpeedX, ballSpeedY
    ball.center = (screenWidth/2, screenHeight/2)
    ballSpeedY *= random.choice((1,-1))
    ballSpeedX *= random.choice((1,-1))

running = True
opponentLevel = random.randrange (1, 4, 1)
opponentTimer = opponentLevel

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerYSpeed += 7

            if event.key == pygame.K_UP:
                playerYSpeed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                playerYSpeed -= 7

            if event.key == pygame.K_UP:
                playerYSpeed += 7

    playerAnimation()

    opponentTimer -= 1
    if opponentTimer == 0:
        opponentAnimation()
        opponentTimer = opponentLevel

    moveBall()

    screen.fill (bgColour)
    showScore (playerScoreX, playerScoreY, opponentScoreX, opponentScoreY)

    pygame.draw.rect(screen, lightGrey, player)
    pygame.draw.rect(screen, lightGrey, opponent)
    pygame.draw.ellipse(screen, lightGrey, ball)
    pygame.draw.aaline (screen, lightGrey, (screenWidth/2,0), (screenWidth/2, screenHeight))

    pygame.display.flip()

    clock.tick(60)
