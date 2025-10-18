#!/usr/bin/env python3
"""
Simple test to verify bold text is working
"""
import pygame
import pygame_gui

pygame.init()

# Small test window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bold Text Test - Press ESC to exit")

# Create manager with theme
manager = pygame_gui.UIManager((800, 600), 'theme.json')

# Test normal and bold text
normal_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect(50, 50, 200, 30),
    text="Normal Text",
    manager=manager
)

bold_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect(50, 100, 200, 30),
    text="Bold Text",
    manager=manager,
    object_id='#bold_label'
)

# Test text box with bold content
text_box = pygame_gui.elements.UITextBox(
    html_text="<b>This is bold text in a text box</b>",
    relative_rect=pygame.Rect(50, 150, 300, 100),
    manager=manager
)

clock = pygame.time.Clock()
running = True

print("Bold text test running. Compare the text styles in the window.")
print("- First line: Normal text")
print("- Second line: Bold text (using theme)")
print("- Text box: Bold text (using HTML)")

while running:
    time_delta = clock.tick(60) / 1000.0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        
        manager.process_events(event)
    
    manager.update(time_delta)
    
    screen.fill((200, 200, 200))  # Light gray background
    manager.draw_ui(screen)
    pygame.display.flip()

pygame.quit()
print("Bold text test completed!")