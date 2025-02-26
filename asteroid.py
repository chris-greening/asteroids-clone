import pygame
import random
import math
from config import WIDTH, HEIGHT, WHITE

class Asteroid:
    def __init__(self):
        """Generate an asteroid with random jagged edges."""
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.size = random.randint(30, 80)  # Define the asteroid size
        self.sides = random.randint(7, 12)  # Number of points
        self.jitter_amount = self.size // 3  # Edge variation
        self.angle = random.uniform(0, 360)  # Movement direction
        self.speed = random.uniform(1, 3)  # Movement speed
        self.shape = self._generate_jagged_shape()

    def _generate_jagged_shape(self):
        """Creates a jagged asteroid shape as a list of points."""
        points = []
        for i in range(self.sides):
            angle = (i / self.sides) * 2 * math.pi  # Distribute points in a circle
            jitter = random.randint(-self.jitter_amount, self.jitter_amount)  # Randomized edges
            radius = self.size + jitter  # Adjusted radius
            x = self.x + math.cos(angle) * radius
            y = self.y + math.sin(angle) * radius
            points.append((x, y))
        return points

    def update(self):
        """Moves the asteroid across the screen."""
        angle_rad = math.radians(self.angle)
        dx = math.cos(angle_rad) * self.speed
        dy = math.sin(angle_rad) * self.speed
        self.x = (self.x + dx) % WIDTH
        self.y = (self.y + dy) % HEIGHT

        # Move shape points accordingly
        self.shape = [(x + dx, y + dy) for x, y in self.shape]

    def draw(self, screen):
        """Draws the asteroid with an outline only (no fill)."""
        pygame.draw.polygon(screen, WHITE, self.shape, 1)  # Wireframe look
