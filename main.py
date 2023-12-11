from pygame import *


window = display.set_mode((700, 500))
display.set_caption("Asteroids")

clock = time.Clock()

game = True
finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, GImage, x, y, width, height, speed):
        super().__init__()
        self.width = width
        self.height = height
        self.image = transform.scale(image.load(GImage), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x >= 0:
            self.rect.x -= self.speed

        if keys[K_RIGHT] and self.rect.x <= 635:
            self.rect.x += self.speed

    def fire(self):
        pass

background = transform.scale(image.load("galaxy.jpg"), (700, 500))

ship = Player("rocket.png", 20, 400, 65, 95, 8)



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0,0))
        ship.draw()
        ship.update()

    display.update()
    clock.tick(60)