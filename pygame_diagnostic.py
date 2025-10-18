#!/usr/bin/env python3
"""
Diagnostic script to check pygame and system capabilities
"""
import pygame
import sys
import os

print("=== Pygame Diagnostics ===")
print(f"Python version: {sys.version}")
print(f"Operating system: {os.name}")

try:
    pygame.init()
    print(f"Pygame version: {pygame.version.ver}")
    print(f"SDL version: {pygame.version.SDL}")
    
    # Check video driver
    print(f"Video driver: {pygame.display.get_driver()}")
    
    # Check available display modes
    info = pygame.display.Info()
    print(f"Display info: {info.current_w}x{info.current_h}, {info.bitsize}-bit")
    
    # Check mixer capabilities
    pygame.mixer.init()
    print(f"Mixer frequency: {pygame.mixer.get_init()}")
    
    # Test basic display creation
    test_screen = pygame.display.set_mode((800, 600))
    print("✓ Basic display creation: SUCCESS")
    pygame.quit()
    
    print("\n=== All tests passed! ===")
    
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    print(f"Error type: {type(e).__name__}")
    
    # Check if it's the specific vstuc error
    if "vstuc" in str(e).lower():
        print("\n🔍 VSTUC Error Detected!")
        print("This is likely a video codec issue.")
        print("Potential solutions:")
        print("1. Update graphics drivers")
        print("2. Try running with different SDL video driver")
        print("3. Disable hardware acceleration")

if __name__ == "__main__":
    print("Run this script to diagnose pygame issues")