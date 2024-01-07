import pygame
import random

# Inizializzazion Pygame
pygame.init()

# Definizione costanti
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Creazione finestra di gioco
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Creazione macchina
car = pygame.Rect(WIDTH // 2, HEIGHT - 50, 50, 50)

# Creazione lista ostacoli
obstacles = []

# Inizializzazione tempo
clock = pygame.time.Clock()

# Ciclo gioco
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimento macchina
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car.left > 0:
        car.x -= 5
    if keys[pygame.K_RIGHT] and car.right < WIDTH:
        car.x += 5

    # Aggiornamento ostacoli
    for obstacle in obstacles:
        obstacle.y += 5
        if obstacle.colliderect(car):
            running = False
        if obstacle.y > HEIGHT:
            obstacles.remove(obstacle)

    # Generazione casuale ostacoli
    if random.randrange(100) < 5:
        obstacle = pygame.Rect(random.randrange(WIDTH - 50), -50, 50, 50)
        obstacles.append(obstacle)

    # Pulizia schermo
    screen.fill(WHITE)

    # Disegno macchina
    pygame.draw.rect(screen, RED, car)

    # Disegno ostacoli
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle)

    # Aggiornamento schermo
    pygame.display.flip()

    # Impostazione fps
    clock.tick(FPS)

# Uscita dal gioco
pygame.quit()
