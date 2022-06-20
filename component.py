import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill("grey")
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        pass


class Player(Tile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y)
        self.image.fill("red")
        self.collide = False

        # Player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 5

    def get_input(self):
        keys = pygame.key.get_pressed()
        # Player movement
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.direction.y = 0

        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.direction.y = 0

        elif keys[pygame.K_UP]:
            self.direction.x = 0
            self.direction.y = -1

        elif keys[pygame.K_DOWN]:
            self.direction.x = 0
            self.direction.y = 1

        else:
            self.direction.x = 0
            self.direction.y = 0

    def move(self, direction):
        # Player movement
        if direction == "right":
            self.direction.x = 1

        elif direction == "left":
            self.direction.x = -1

        elif direction == "up":
            self.direction.y = -1

        elif direction == "down":
            self.direction.y = 1

        else:
            self.direction.x = 0
            self.direction.y = 0

    # def move(self):
    #     self.rect.x += self.direction.x * self.speed
    #     self.rect.y += self.direction.y * self.speed

    def update(self):
        self.get_input()
