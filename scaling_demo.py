#!/usr/bin/env python3
"""
Simple test to demonstrate resolution scaling in action
"""

import pygame
import pygame_gui

pygame.init()

# Test with a smaller window to demonstrate scaling
TEST_WIDTH = 1280
TEST_HEIGHT = 720

# Reference resolution (1920x1080)
REFERENCE_WIDTH = 1920
REFERENCE_HEIGHT = 1080

# Calculate scaling factors
scale_x = TEST_WIDTH / REFERENCE_WIDTH
scale_y = TEST_HEIGHT / REFERENCE_HEIGHT
scale_factor = min(scale_x, scale_y)

# For positioning, we use the reference resolution
width = REFERENCE_WIDTH
height = REFERENCE_HEIGHT

print(f"Test window: {TEST_WIDTH}x{TEST_HEIGHT}")
print(f"Reference resolution: {REFERENCE_WIDTH}x{REFERENCE_HEIGHT}")
print(f"Scale factor: {scale_factor:.3f}")

def scale_coord(coord):
    """Scale a single coordinate"""
    return int(coord * scale_factor)

def scale_size(w, h):
    """Scale width and height"""
    return int(w * scale_factor), int(h * scale_factor)

def scale_pos(x, y):
    """Scale position coordinates"""
    return int(x * scale_factor), int(y * scale_factor)

# Create screen and UI manager
screen = pygame.display.set_mode((TEST_WIDTH, TEST_HEIGHT))
pygame.display.set_caption("Scaling Test - Press ESC to exit")
manager = pygame_gui.UIManager((TEST_WIDTH, TEST_HEIGHT))

# Create some test UI elements using the original 1920x1080 coordinates
# These should scale properly to the 1280x720 window

# Title (centered at top)
title_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(scale_pos(width//2 - 200, 100), scale_size(400, 80)),
    text="Scaling Test",
    manager=manager
)

# Play button (center left)
play_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(scale_pos(width//2 - 320, int(3 * height / 4)), scale_size(200, 100)),
    text="Play",
    manager=manager
)

# Instructions button (center)
instructions_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(scale_pos(width//2 - 90, int(3 * height / 4) + 10), scale_size(180, 80)),
    text="Instructions",
    manager=manager
)

# Quit button (center right)
quit_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(scale_pos(width//2 + 105, int(3 * height / 4) + 10), scale_size(180, 80)),
    text="Quit",
    manager=manager
)

# Info panel
info_panel = pygame_gui.elements.UIPanel(
    relative_rect=pygame.Rect(scale_pos(50, 50), scale_size(400, 200)),
    manager=manager
)

info_text = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((10, 10), (380, 180)),
    text=f"Window: {TEST_WIDTH}x{TEST_HEIGHT}\nReference: {REFERENCE_WIDTH}x{REFERENCE_HEIGHT}\nScale: {scale_factor:.3f}\n\nUI elements are positioned using\n1920x1080 coordinates but\nscaled to fit this window.",
    manager=manager,
    container=info_panel
)

clock = pygame.time.Clock()
running = True

print("Window created successfully. UI elements should be properly scaled.")
print("Close the window or press ESC to exit.")

while running:
    time_delta = clock.tick(60) / 1000.0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == quit_button:
                running = False
            else:
                print(f"Button pressed: {event.ui_element.text}")
        
        manager.process_events(event)
    
    manager.update(time_delta)
    
    screen.fill((50, 50, 100))  # Dark blue background
    manager.draw_ui(screen)
    pygame.display.flip()

pygame.quit()
print("Scaling test completed!")