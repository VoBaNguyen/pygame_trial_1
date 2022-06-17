import pygame
from settings import screen_width, screen_height, x_tiles, y_tiles, tile_size
from component import Tile, Player


class Layout:

    def __init__(self, surface):

        # Setup boundary
        self.display_surface = surface
        self.current_x = 0

        # Layout setup
        self.boundary_tiles = self.create_boundary_tiles()
        self.player = pygame.sprite.GroupSingle()
        player_sprite = Player(tile_size, 3*tile_size, 3*tile_size)
        self.player.add(player_sprite)

    def create_boundary_tiles(self):
        boundary_tiles = pygame.sprite.Group()
        for row_index in range(x_tiles):
            if row_index == 0 or row_index == (y_tiles-1):
                for col_index in range(x_tiles):
                    x = tile_size * col_index
                    y = tile_size * row_index
                    tile = Tile(tile_size, x, y)
                    boundary_tiles.add(tile)
            else:
                for col_index in [0, x_tiles-1]:
                    x = tile_size * col_index
                    y = tile_size * row_index
                    tile = Tile(tile_size, x, y)
                    boundary_tiles.add(tile)

        return boundary_tiles

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.boundary_tiles:
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    self.current_x = player.rect.right

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.rect.y += player.direction.y * player.speed

        for sprite in self.boundary_tiles:
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.direction.y = 0
                    player.rect.bottom = sprite.rect.top
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def create_player(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

    def run(self):
        self.boundary_tiles.draw(self.display_surface)

        # Update player position before draw
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.update()
        self.player.draw(self.display_surface)
