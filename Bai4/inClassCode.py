# đây là file chúng ta đã code được tại lớp

import pygame
import random

class Paddle:
    def __init__(self, x, y, width, height, screen_height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 20
        self.screen_height = screen_height
        
    def move_up(self):
        self.y -= self.speed
        if self.y < 0:
            self.y = 0
            
    def move_down(self):
        self.y += self.speed
        if self.y + self.height > self.screen_height:
            self.y = self.screen_height - self.height
            
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))


class MainGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.player1 = Paddle(50, self.height / 2, 30, 120, self.height)
        self.player2 = Paddle(self.width - 50, self.height / 2, 30, 120, self.height)
        
    def drawFullGame(self, screen):
        screen.fill((0, 0, 0))
        
        self.player1.draw(screen)
        self.player2.draw(screen)
        
        pygame.display.update()
        
    def handle_user_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: #K_w
                    self.player2.move_up() # tính trừu tượng
                if event.key == pygame.K_DOWN:
                    self.player2.move_down()
                    
      
pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Pong")

mainGame = MainGame(1200, 800)

while True:
    
    mainGame.handle_user_event()
    
    mainGame.drawFullGame(screen)
    
    pygame.time.Clock().tick(60)

pygame.quit()