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
    print(genomes)
    # Setup Neat
    global GEN
    GEN += 1
    nets = []
    ge = []
    players = []

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        g.fitness = 0
        ge.append(g)
        # Create new player
        player = pygame.sprite.GroupSingle()
        player.add(Player(tile_size, 3*tile_size, 3*tile_size))
        players.append(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for x, player in enumerate(players):
            ge[x].fitness += 0.1
            print("== == == == == == == == == == =")
            print(nets[x].input_nodes)
            print(nets[x].node_evals)
            # print(player.sprite.rect.y)
            # output = nets[x].activate((player.sprite.rect.y, abs(
            #     bird.y - pipes[pipe_indx].height), abs(bird.y - pipes[pipe_indx].bottom)))
            # if output[0] > 0.5:
            player.sprite.move("right")

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
