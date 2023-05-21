import pygame, random

WIDTH = 800
HEIGHT = 600

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Catch the Karbownik")
icon = pygame.image.load("icon.jpeg")
pygame.display.set_icon(icon)

background = pygame.image.load("background.png")

target = pygame.image.load("karbownik1.png")

target_x = 400
target_y = 300

def draw_target(x, y):
    screen.blit(target, (x, y))

score = 0

font = pygame.font.SysFont("arial", 32)

def show_score():
    score_text = font.render("Punkty: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

running = True

while running:

    screen.fill((0, 0, 0))

    screen.blit(background, (0, 0))

    photo_number = random.randint(1,4)
    
    draw_target(target_x, target_y)

    show_score()

    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_x, mouse_y = pygame.mouse.get_pos()

            if target_x <= mouse_x <= target_x + target.get_width() and target_y <= mouse_y <= target_y + target.get_height():

                score += 1

                target_x = random.randint(0, WIDTH - target.get_width())
                target_y = random.randint(0, HEIGHT - target.get_height())

                new_target_x = random.randint(0, WIDTH - target.get_width())
                new_target_y = random.randint(0, HEIGHT - target.get_height())
                target = pygame.image.load("karbownik"+str(photo_number)+".png")
                draw_target(new_target_x, new_target_y)