import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
FALLING_OBJECT_WIDTH = 50
FALLING_OBJECT_HEIGHT = 50
FALLING_OBJECT_SPEED = 5
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dodge the Falling Objects")

# Player class
class Player:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    def move(self, dx):
        self.rect.x += dx
        # Keep player within screen bounds
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > SCREEN_WIDTH - PLAYER_WIDTH:
            self.rect.x = SCREEN_WIDTH - PLAYER_WIDTH

    def draw(self):
        pygame.draw.rect(screen, GREEN, self.rect)

# Falling object class
class FallingObject:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, SCREEN_WIDTH - FALLING_OBJECT_WIDTH), 0, FALLING_OBJECT_WIDTH, FALLING_OBJECT_HEIGHT)

    def fall(self):
        self.rect.y += FALLING_OBJECT_SPEED

    def draw(self):
        pygame.draw.rect(screen, RED, self.rect)

# Main game function
def main():
    clock = pygame.time.Clock()
    player = Player()
    falling_objects = []
    score = 0
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-5)
        if keys[pygame.K_RIGHT]:
            player.move(5)

        # Create new falling objects
        if random.randint(1, 20) == 1:  # Adjust frequency of falling objects
            falling_objects.append(FallingObject())

        # Update falling objects
        for obj in falling_objects:
            obj.fall()
            if obj.rect.colliderect(player.rect):
                game_over = True  # End game if player is hit
            if obj.rect.y > SCREEN_HEIGHT:
                falling_objects.remove(obj)  # Remove off-screen objects

        # Draw everything
        screen.fill(WHITE)
        player.draw()
        for obj in falling_objects:
            obj.draw()

        # Update score
        score += 1  # Increase score over time

        # Display score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    # Game over screen
    screen.fill(WHITE)
    game_over_text = font.render("Game Over!", True, (255, 0, 0))
    final_score_text = font.render(f"Final Score: {score}", True, (0, 0, 0))
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 20))
    screen.blit(final_score_text, (SCREEN_WIDTH // 2 - 70, SCREEN_HEIGHT // 2 + 20))
    pygame.display.flip()
    pygame.time.wait(3000)  # Wait for 3 seconds before quitting

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()