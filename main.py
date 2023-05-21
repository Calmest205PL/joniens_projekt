# Import pygame library
import pygame, random

WIDTH = 800
HEIGHT = 600

# Initialize pygame
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title and icon of the window
pygame.display.set_caption("Catch the Karbownik")
icon = pygame.image.load("icon.jpeg")
pygame.display.set_icon(icon)

# Load the background image
background = pygame.image.load("background.png")

# Load the target image
target = pygame.image.load("karbownik1.png")

# Define the target position
target_x = 400
target_y = 300

# Define a function to draw the target on the screen
def draw_target(x, y):
    screen.blit(target, (x, y))

# Define a variable to store the score
score = 0

# Define a font to render the score text
font = pygame.font.SysFont("arial", 32)

# Define a function to show the score on the screen
def show_score():
    score_text = font.render("Punkty: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

# Define a variable to store the game loop condition
running = True

# Start the game loop
while running:

    # Fill the screen with black color
    screen.fill((0, 0, 0))

    # Draw the background image on the screen
    screen.blit(background, (0, 0))

    # Draw the target on the screen
    photo_number = random.randint(1,4)
    
    draw_target(target_x, target_y)

    # Show the score on the screen
    show_score()

    # Update the display
    pygame.display.update()

    # Loop through the events in the event queue
    for event in pygame.event.get():

        # If the event is QUIT, exit the game loop
        if event.type == pygame.QUIT:
            running = False

        # If the event is MOUSEBUTTONDOWN, check if the mouse position is on the target
        if event.type == pygame.MOUSEBUTTONDOWN:

            # Get the mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check if the mouse position is within the target rectangle
            if target_x <= mouse_x <= target_x + target.get_width() and target_y <= mouse_y <= target_y + target.get_height():

                # Increase the score by one
                score += 1

                # Move the target to a random position on the screen
                target_x = random.randint(0, WIDTH - target.get_width())
                target_y = random.randint(0, HEIGHT - target.get_height())

                # Draw another target on a random position on the screen
                new_target_x = random.randint(0, WIDTH - target.get_width())
                new_target_y = random.randint(0, HEIGHT - target.get_height())
                target = pygame.image.load("karbownik"+str(photo_number)+".png")
                draw_target(new_target_x, new_target_y)
