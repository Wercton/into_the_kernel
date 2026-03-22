import pygame as pg
from src.config import WIDTH, HEIGHT, MAP
from src.game.renderer import draw_map


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Into the Kernel")
        self.clock = pg.time.Clock()
        self.running = True

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def update(self):
        pass  # lógica futura (player, turnos, IA)

    def render(self):
        self.screen.fill((0, 0, 0))
        draw_map(self.screen, MAP)
        pg.display.flip()

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.render()

        pg.quit()