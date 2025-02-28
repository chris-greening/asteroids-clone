import pygame
import random

def apply_crt_effect(screen):
    """Apply CRT effect to the screen"""
    _apply_scanlines(screen)
    _apply_pixelation(screen, scale_factor=2)
    _apply_flicker(screen)
    _apply_glow(screen)

def _apply_scanlines(screen):
    """Draws horizontal scanlines to simulate an old CRT screen."""
    width, height = screen.get_size()
    scanline_surface = pygame.Surface((width, height), pygame.SRCALPHA)

    for y in range(0, height, 4):  # Every 4 pixels (adjust for intensity)
        pygame.draw.line(scanline_surface, (0, 0, 0, 60), (0, y), (width, y))  # Semi-transparent black

    screen.blit(scanline_surface, (0, 0))

def _apply_pixelation(screen, scale_factor=4):
    """Reduces resolution slightly to create a pixelated effect."""
    width, height = screen.get_size()
    small_surf = pygame.transform.scale(screen, (width // scale_factor, height // scale_factor))
    screen.blit(pygame.transform.scale(small_surf, (width, height)), (0, 0))

def _apply_flicker(screen):
    """Adds a subtle flicker to simulate an old CRT glow effect."""
    if random.randint(0, 20) == 0:  # 10% chance per frame
        flicker_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        flicker_surface.fill((255, 255, 255, 5))  # Slight white overlay
        screen.blit(flicker_surface, (0, 0))

def _apply_glow(screen):
    """Creates a soft glow effect by blurring bright pixels."""
    width, height = screen.get_size()

    # Create a blurred surface
    glow_surf = pygame.transform.smoothscale(screen, (width // 2, height // 2))
    glow_surf = pygame.transform.smoothscale(glow_surf, (width, height))

    # Overlay with transparency
    glow_surf.set_alpha(100)  # Adjust glow intensity (higher = stronger glow)
    screen.blit(glow_surf, (0, 0))