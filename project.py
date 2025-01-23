import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithms Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

# Fonts
font = pygame.font.Font(None, 36)

# Settings
BAR_WIDTH = 60
BAR_GAP = 10
NUM_BARS = 6
FPS = 60
sorted_color = GREEN
unsorted_color = BLUE

# Generate random bars
def generate_bars():
    return [random.randint(50, 300) for _ in range(NUM_BARS)]

# Draw bars
def draw_bars(bars, selected=None):
    screen.fill(WHITE)
    for i, height in enumerate(bars):
        x = i * (BAR_WIDTH + BAR_GAP) + 100
        y = HEIGHT - height - 50
        color = sorted_color if bars == sorted(bars) else unsorted_color
        if selected is not None and i == selected:
            color = RED
        pygame.draw.rect(screen, color, (x, y, BAR_WIDTH, height))
        # Display numbers on top of bars
        text = font.render(str(height), True, BLACK)
        screen.blit(text, (x + 10, y - 30))
    pygame.display.flip()

# Game loop
def game_loop():
    bars = generate_bars()
    selected = None
    clock = pygame.time.Clock()
    game_running = True

    while game_running:
        clock.tick(FPS)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if selected is None:
                    selected = (pygame.mouse.get_pos()[0] // (BAR_WIDTH + BAR_GAP)) - 1
                else:
                    new_selected = (pygame.mouse.get_pos()[0] // (BAR_WIDTH + BAR_GAP)) - 1
                    if 0 <= selected < len(bars) and 0 <= new_selected < len(bars):
                        # Swap bars
                        bars[selected], bars[new_selected] = bars[new_selected], bars[selected]
                    selected = None

        draw_bars(bars, selected)

        # Check win condition
        if bars == sorted(bars):
            screen.fill(WHITE)
            win_text = font.render("You Win! Press Q to Quit.", True, BLACK)
            screen.blit(win_text, (WIDTH // 2 - 150, HEIGHT // 2 - 20))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_running = False

# Run the game
game_loop()
pygame.quit()
sys.exit()
