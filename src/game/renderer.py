import pygame as pg
from src.config import TILE_SIZE, COLORS


def draw_map(screen, game_map):
    for row, line in enumerate(game_map):
        for col, tile in enumerate(line):
            color = COLORS.get(tile, (255, 0, 255))  # fallback debug

            rect = pg.Rect(
                col * TILE_SIZE,
                row * TILE_SIZE,
                TILE_SIZE,
                TILE_SIZE,
            )

            pg.draw.rect(screen, color, rect)
