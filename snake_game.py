import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

font = pygame.font.SysFont("arial", 25)

def show_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def game_over():
    screen.fill(BLACK)
    over_font = pygame.font.SysFont("arial", 40)
    over_text = over_font.render(f"GAME OVER! Score: {score}", True, RED)
    screen.blit(over_text, (WIDTH // 6, HEIGHT // 2))
    pygame.display.update()
    pygame.time.delay(2000)  


BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

snake = [[100, 100], [80, 100], [60, 100]]
direction = "RIGHT"

# Food position (random, aligned to grid)
def random_food_pos():
    x = random.randrange(0, WIDTH, BLOCK_SIZE)
    y = random.randrange(0, HEIGHT, BLOCK_SIZE)
    return [x, y]

food = random_food_pos()
score = 0

def draw_snake(snake):
    for block in snake:
        pygame.draw.rect(screen, GREEN, (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    head = list(snake[0])
    if direction == "UP":
        head[1] -= BLOCK_SIZE
    elif direction == "DOWN":
        head[1] += BLOCK_SIZE
    elif direction == "LEFT":
        head[0] -= BLOCK_SIZE
    elif direction == "RIGHT":
        head[0] += BLOCK_SIZE

    # Check collision with walls
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        game_over()
        running = False

    snake.insert(0, head)

# Check collision with itself
    if head in snake[1:]:
        game_over()
        running = False

    # Check if snake ate food
    if head == food:
        score += 1
        food = random_food_pos()
    else:
        snake.pop()  # only remove tail if food NOT eaten

    screen.fill(BLACK)
    draw_snake(snake)
    pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))
    show_score(score)
    pygame.display.update()
    clock.tick(10)

pygame.quit()
sys.exit()
