# ICD2O Setup Check
# Run this first. If you see the green window, your machine is ready.

import sys

print("Python version:", sys.version)

import pygame

print("pygame version:", pygame.version.ver)

pygame.init()
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Setup Check: close this window when you see it")
screen.fill((0, 150, 80))
pygame.display.flip()
pygame.event.pump()
pygame.time.wait(3000)
pygame.quit()

print("Setup check passed. You are ready to build.")
