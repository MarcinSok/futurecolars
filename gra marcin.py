import pygame
import random

pygame.init()

# rozmiar okna gry
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# kolory RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# utworzenie okna gry
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Strzelanka 3D")

# klasa gracza
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2

    def update(self, movement):
        self.rect.x += movement[pygame.K_RIGHT] - movement[pygame.K_LEFT]
        self.rect.y += movement[pygame.K_DOWN] - movement[pygame.K_UP]

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

# klasa wroga
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(SCREEN_HEIGHT - self.rect.height)

    def update(self):
        pass

# grupy sprite'ów
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# utworzenie gracza
player = Player()
all_sprites.add(player)

# utworzenie wrogów
for i in range(10):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# główna pętla gry
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # poruszanie gracza
    keys = pygame.key.get_pressed()
    player.update(keys)

    # aktualizacja wrogów
    for enemy in enemies:
        enemy.update()

    # rysowanie sprite'ów na ekranie
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # wyświetlenie okna gry
    pygame.display.flip()

# zakończenie gry
pygame.quit()
