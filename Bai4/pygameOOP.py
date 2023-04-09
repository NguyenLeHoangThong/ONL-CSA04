# đây là file hoàn chỉnh trò chơi

import pygame
import random

class Ball:
    def __init__(self, x, y, radius, screen_width, screen_height):
        self.x = x
        self.y = y
        self.radius = radius
        self.direction = random.choice([(1,1), (1,-1), (-1,1), (-1,-1)])
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed = 5

    def move(self):
        self.x += self.speed * self.direction[0]
        self.y += self.speed * self.direction[1]

    def bounce(self):
        self.direction = (self.direction[0], -self.direction[1])

    def reset(self):
        self.x = self.screen_width/2
        self.y = self.screen_height/2
        self.direction = random.choice([(1,1), (1,-1), (-1,1), (-1,-1)])

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius)

class Paddle:
    def __init__(self, x, y, width, height, screen_width, screen_height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed = 20

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

class Pong:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.ball = Ball(self.width/2, self.height/2, 10, self.width, self.height)
        self.player1 = Paddle(50, self.height/2 - 40, 10, 80, self.width, self.height)
        self.player2 = Paddle(self.width - 60, self.height/2 - 40, 10, 80, self.width, self.height)
        self.score1 = 0
        self.score2 = 0
        self.font = pygame.font.SysFont("Arial", 50)

    def update_game_state(self):
        # Move the ball
        self.ball.move()

        # Check for collisions with walls
        if self.ball.y - self.ball.radius < 0 or self.ball.y + self.ball.radius > self.height:
            self.ball.bounce()

        # Check for collisions with paddles
        if (self.ball.x - self.ball.radius < self.player1.x + self.player1.width and
            self.ball.x + self.ball.radius > self.player1.x and
            self.ball.y + self.ball.radius > self.player1.y and
            self.ball.y - self.ball.radius < self.player1.y + self.player1.height):
            self.ball.bounce()
            self.ball.direction = (abs(self.ball.direction[0]), self.ball.direction[1])

        if (self.ball.x + self.ball.radius > self.player2.x and
            self.ball.x - self.ball.radius < self.player2.x + self.player2.width and
            self.ball.y + self.ball.radius > self.player2.y and
            self.ball.y - self.ball.radius < self.player2.y + self.player2.height):
            self.ball.bounce()
            self.ball.direction = (-abs(self.ball.direction[0]), self.ball.direction[1])

        # Check for collisions with goals
        if self.ball.x < 0:
            self.score2 += 1
            self.ball.reset()
        elif self.ball.x > self.width:
            self.score1 += 1
            self.ball.reset()

    def draw(self, screen):
        # Draw the background
        screen.fill((0, 0, 0))

        # Draw the paddles and ball
        self.player1.draw(screen)
        self.player2.draw(screen)
        self.ball.draw(screen)

        # Draw the scores
        score1_text = self.font.render(str(self.score1), True, (255, 255, 255))
        screen.blit(score1_text, (self.width/4 - score1_text.get_width()/2, 50))

        score2_text = self.font.render(str(self.score2), True, (255, 255, 255))
        screen.blit(score2_text, (3*self.width/4 - score2_text.get_width()/2, 50))

        # Update the display
        pygame.display.update()
        
    def handle_events(self):
        # Xử lý các sự kiện trong trò chơi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.player1.move_up()
                elif event.key == pygame.K_s:
                    self.player1.move_down()
                elif event.key == pygame.K_UP:
                    self.player2.move_up()
                elif event.key == pygame.K_DOWN:
                    self.player2.move_down()
                    
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

pong = Pong(SCREEN_WIDTH, SCREEN_HEIGHT)

while True:
    pong.handle_events()

    pong.update_game_state()

    pong.draw(screen)

    pygame.time.Clock().tick(60)

pygame.quit()