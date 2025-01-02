import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

# Colors
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption('Flappy Bird')

# Load images
bird_image = pygame.image.load('bird.png')
pipe_image = pygame.image.load('pipe.png')
background_image = pygame.image.load('background.png')

# Scale images if necessary
bird_image = pygame.transform.scale(bird_image, (50, 35))
pipe_image = pygame.transform.scale(pipe_image, (80, 500))
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load sounds 
class Bird:
    def __init__(self):
        self.image = bird_image
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.y_speed = 0
        self.gravity = 0.5
        self.lift = -10

    def update(self):
        self.y_speed += self.gravity
        self.y += self.y_speed

        # Prevent bird from going out of bounds
        if self.y > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT
            self.y_speed = 0
        if self.y < 0:
            self.y = 0
            self.y_speed = 0

    def flap(self):
        self.y_speed = self.lift

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

class Pipe:
    def __init__(self):
        self.image = pipe_image
        self.x = SCREEN_WIDTH
        self.y = random.randint(-200, 0)
        self.speed = 3

    def update(self):
        self.x -= self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        screen.blit(pygame.transform.flip(self.image, False, True), (self.x, self.y + self.image.get_height() + 150))

    def off_screen(self):
        return self.x < -self.image.get_width()

    def collide(self, bird):
        bird_rect = pygame.Rect(bird.x, bird.y, bird.image.get_width(), bird.image.get_height())
        pipe_rect_top = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        pipe_rect_bottom = pygame.Rect(self.x, self.y + self.image.get_height() + 150, self.image.get_width(), self.image.get_height())

        return bird_rect.colliderect(pipe_rect_top) or bird_rect.colliderect(pipe_rect_bottom)
def display_score(screen, score):
    font = pygame.font.SysFont(None, 35)
    score_surface = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_surface, (10, 10))

def show_game_over(screen):
    font = pygame.font.SysFont(None, 55)
    game_over_surface = font.render('Game Over', True, (255, 0, 0))
    game_over_rect = game_over_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50))
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

def show_retry_button(screen):
    font = pygame.font.SysFont(None, 45)
    retry_surface = font.render('Retry', True, WHITE)
    retry_rect = retry_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50))
    pygame.draw.rect(screen, (0, 0, 0), retry_rect.inflate(20, 10))
    screen.blit(retry_surface, retry_rect)
    pygame.display.flip()
    return retry_rect
def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        bird = Bird()
        pipes = []
        score = 0
        game_over = False

        while not game_over and running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bird.flap()
                        flap_sound.play()

            bird.update()

            if len(pipes) == 0 or pipes[-1].x < SCREEN_WIDTH - 200:
                pipes.append(Pipe())

            for pipe in pipes:
                pipe.update()
                if pipe.collide(bird):
                    hit_sound.play()
                    game_over = True
                if pipe.off_screen():
                    pipes.remove(pipe)
                    score += 1

            screen.blit(background_image, (0, 0))
            bird.draw(screen)
            for pipe in pipes:
                pipe.draw(screen)

            display_score(screen, score)

            pygame.display.flip()
            clock.tick(30)

            if game_over:
                show_game_over(screen)
                retry_rect = show_retry_button(screen)
                break

        # Wait for player to press retry button
        while game_over and running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_over = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if retry_rect.collidepoint(event.pos):
                        game_over = False

    pygame.quit()

if __name__ == "__main__":
    main()
