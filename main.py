import pygame
import neat
import os
from settings import screen_width, screen_height, tile_size
import sys
from layout import Layout
from component import Player

# NEAT GLOBAL VAR
GEN = 0


# SETUP PYGAME
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
layout = Layout(screen)


def main(genomes, config):
    # Setup Neat
    global GEN
    GEN += 1
    nets = []
    ge = []
    players = []
    run = True

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        g.fitness = 0
        ge.append(g)
        # Create new player
        player = pygame.sprite.GroupSingle()
        player.add(Player(tile_size, 3*tile_size, 3*tile_size))
        players.append(player)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if len(players) == 0:
            run = False

        for x, player in enumerate(players):
            ge[x].fitness += 0.1

            a1, a2 = nets[x].activate(
                [abs(player.sprite.rect.x - screen_width/2), abs(player.sprite.rect.x - screen_height/2)])
            # a1, a2 = nets[x].activate((0, 0))
            # print(a1, a2)
            if a1 > 0:
                player.sprite.move("right")
            else:
                player.sprite.move("left")

            if a2 > 0:
                player.sprite.move("down")
            else:
                player.sprite.move("up")

        for x, player in enumerate(players):
            if player.sprite.collide:
                players.pop(x)

        screen.fill('black')
        layout.run(players)

        pygame.display.update()
        clock.tick(60)


def run(config_path):
    import pickle

    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(main, 50)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run(config_path)
