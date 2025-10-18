#!/usr/bin/env python3
"""
Test script to verify the scaling system works correctly
"""

# Simulate different screen resolutions
test_resolutions = [
    (1920, 1080),  # Original resolution
    (1366, 768),   # Common laptop resolution
    (1280, 720),   # 720p
    (2560, 1440),  # 1440p
    (3840, 2160),  # 4K
]

REFERENCE_WIDTH = 1920
REFERENCE_HEIGHT = 1080

def test_scaling(actual_width, actual_height):
    """Test scaling for a given resolution"""
    print(f"\nTesting resolution: {actual_width}x{actual_height}")
    
    # Calculate scaling factors
    scale_x = actual_width / REFERENCE_WIDTH
    scale_y = actual_height / REFERENCE_HEIGHT
    scale_factor = min(scale_x, scale_y)
    
    print(f"Scale factor: {scale_factor:.3f}")
    
    # Test some common game coordinates
    test_coords = [
        (960, 540),    # Center of screen
        (480, 270),    # Quarter screen
        (1440, 810),   # Three quarters
        (100, 100),    # Top left area
        (1820, 980),   # Bottom right area
    ]
    
    print("Original -> Scaled coordinates:")
    for x, y in test_coords:
        scaled_x = int(x * scale_factor)
        scaled_y = int(y * scale_factor)
        print(f"  ({x:4d}, {y:3d}) -> ({scaled_x:4d}, {scaled_y:3d})")
    
    # Test button sizes
    test_sizes = [
        (200, 100),    # Play button
        (180, 80),     # Instructions button
        (100, 100),    # Profile button
        (1000, 250),   # Title text
    ]
    
    print("Original -> Scaled sizes:")
    for w, h in test_sizes:
        scaled_w = int(w * scale_factor)
        scaled_h = int(h * scale_factor)
        print(f"  ({w:4d}x{h:3d}) -> ({scaled_w:4d}x{scaled_h:3d})")

if __name__ == "__main__":
    print("Resolution Scaling Test")
    print("=" * 50)
    
    for width, height in test_resolutions:
        test_scaling(width, height)
    
    print("\n" + "=" * 50)
    print("Scaling test complete!")