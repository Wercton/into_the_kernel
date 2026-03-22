# modes: normal, insert (i I a A), visual (v), replace (R)
# w e $ 0 M dw dd p P yw x diw

import pygame as pg
from src.config import (
    TILE_SIZE,
    COLS,
    ROWS,
    WIDTH,
    HEIGHT,
    MAP,
    COLORS,
)

pg.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Hello World")

clock = pg.time.Clock()
executando = True

while executando:
    clock.tick(60)
    screen.fill((0, 0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            executando = False

    for row in range(ROWS):
        for col in range(COLS):
            tile = MAP[row][col]
            color = COLORS.get(tile)

            rect = pg.Rect(
                col * TILE_SIZE,
                row * TILE_SIZE,
                TILE_SIZE,
                TILE_SIZE
            )

            pg.draw.rect(screen, color, rect)

    pg.display.flip()

pg.quit()
