import pygame
import random
import math

class GameObject:
    def __init__(self, image_path, x, y):
        self.image = pygame.image.load(image_path)
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def is_collision(self, other):
        distance = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        return distance <= 27

class Rabbit(GameObject):
    def __init__(self, x, y):
        super().__init__('rabbit.png', x, y)
        self.x_change = 0
        self.y_change = 0

    def move(self):
        self.x += self.x_change
        self.y += self.y_change
        self.x = max(0, min(736, self.x))
        self.y = max(0, min(510, self.y))

class Carrot(GameObject):
    def __init__(self):
        super().__init__('carrot.png', random.randint(64, 736), random.randint(0, 510))

class Fox(GameObject):
    def __init__(self):
        super().__init__('fox.png', random.randint(64, 736), random.randint(0, 510))
        self.x_change = 1
        self.y_change = 40

    def move(self):
        self.x += self.x_change
        if self.x <= 0 or self.x >= 736:
            self.x_change *= -1
            self.y += self.y_change
        if self.y > 536:
            self.x = random.randint(64, 736)
            self.y = random.randint(0, 510)

def display_text(screen, text, x, y, size=25, color=(255, 255, 255)):
    font = pygame.font.Font('freesansbold.ttf', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Carrot Chase Game')
    pygame.display.set_icon(pygame.image.load('bear.png'))

    background = pygame.image.load('lesson7_nature.png')
    rabbit = Rabbit(400, 300)
    carrots = [Carrot() for _ in range(15)]
    foxes = [Fox() for _ in range(6)]

    score = 0
    collision_count = 0
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    rabbit.x_change = 2
                elif event.key == pygame.K_LEFT:
                    rabbit.x_change = -2
                elif event.key == pygame.K_UP:
                    rabbit.y_change = -2
                elif event.key == pygame.K_DOWN:
                    rabbit.y_change = 2
            elif event.type == pygame.KEYUP:
                rabbit.x_change = 0
                rabbit.y_change = 0

        screen.blit(background, (0, 0))
        rabbit.move()
        rabbit.draw(screen)

        for carrot in carrots:
            if rabbit.is_collision(carrot):
                carrot.x = random.randint(64, 736)
                carrot.y = random.randint(0, 510)
                if not game_over:
                    score += 1
            carrot.draw(screen)

        for fox in foxes:
            fox.move()
            if rabbit.is_collision(fox):
                fox.x = random.randint(64, 736)
                fox.y = random.randint(0, 510)
                if not game_over:
                    collision_count += 1
                    score -= 1
                if collision_count >= 6:
                    game_over = True
            fox.draw(screen)

        display_text(screen, f'Score: {score}', 400, 10)
        display_text(screen, f'Collisions: {collision_count}', 400, 40)

        if game_over:
            display_text(screen, 'GAME OVER', 400, 300, size=50)
        pygame.display.update()

if __name__ == '__main__':
    main()