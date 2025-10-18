# Copilot Instructions for Strategy Card Game

## Project Overview
This is a two-player, turn-based strategy card game built with Python/Pygame for a Computer Science NEA project. The game features 4 races (Human, Elf, Dwarf, Undead) with unique cards and a deck-building system. **The game now supports resolution-independent scaling while maintaining aspect ratios.**

## Architecture & Core Components

### Resolution Scaling System
- **Reference resolution**: Game designed for 1920x1080
- **Automatic scaling**: Adapts to any screen resolution while preserving aspect ratios
- **Coordinate system**: Use original 1920x1080 coordinates in code; scaling applied automatically
- **Scale factor**: Calculated as `min(actual_width/1920, actual_height/1080)` to maintain proportions

### Scaling Implementation
```python
# Global scaling variables (in setup section)
REFERENCE_WIDTH = 1920
REFERENCE_HEIGHT = 1080
scale_factor = min(actual_width / REFERENCE_WIDTH, actual_height / REFERENCE_HEIGHT)

# Helper functions
scale_coord(coord)     # Scale single coordinate
scale_size(w, h)      # Scale width and height  
scale_pos(x, y)       # Scale position coordinates
```

### Game Structure
- **Single-file architecture**: All code is in `main game.py` (~2130 lines)
- **State-based UI**: Game states include `startup`, `deck`, `instructions`, `playing`, `game_ended`, `pause_menu`
- **Class hierarchy**: `card`, `player`, `game`, `panel`, `button`, `card_button` classes
- **Asset-driven UI**: Heavy reliance on image assets in `ASSETS/` directory structure

### Key Classes & Patterns
- **card class**: Immutable data objects with `clone()` method for deck building
- **player class**: Manages deck/hand/discard_pile, uses `addtodeck()`, `draw_card()`, `discard_card()`
- **UI components**: Custom `panel` and `button` classes wrapping pygame_gui elements with automatic scaling
- **card_button**: Specialized button that holds card references and original coordinates for repositioning

### Asset Organization
```
ASSETS/
├── CARDS/[RACE]/[CardName].png    # Card images by race
├── BUTTONS/[SCREEN]/[action].png  # UI buttons by game state
├── BACKGROUNDS/                   # Background images (auto-scaled to actual screen size)
├── SOUNDTRACKS/                   # Music files
└── TEXT/                         # UI text graphics
```

## Development Patterns

### Resolution-Independent Development
- **Always use 1920x1080 coordinates** when positioning UI elements
- **Scaling is automatic** - panel/button constructors apply scaling internally
- **Original coordinates preserved** - classes store both original and scaled coordinates
- **Background images**: Automatically scaled to actual screen dimensions
- **Asset loading**: Card/UI images scaled proportionally via `scale_size()` helper

### UI State Management
- **Global state**: `active_ui_elements` list tracks all UI for cleanup
- **Screen drawing**: `screen_drawn` flag prevents redraw until state change
- **Element lifecycle**: Always call `element.kill()` and remove from `active_ui_elements` when changing states
- **Coordinate storage**: UI classes store both `original_x/y` (1920x1080) and scaled coordinates

### Event Handling
- **Button identification**: Use `event.ui_element == button_reference` pattern
- **Card selection**: `selected_cards` global list manages multi-card selection
- **Profile switching**: `current_profile` toggles between "P1"/"P2" for deck editing
- **Card movement**: Uses original coordinates for repositioning, scaling applied in `move_to()`

### Game Logic Patterns
- **Turn management**: `check_current_player()` returns current/opponent tuple
- **Card effects**: `apply_card_effect()` processes selected cards, validates energy costs
- **Deck management**: Players start with all 20 cards, use `replenish_deck()` to reset
- **Coordinate handling**: `card_button.getx()/gety()` returns original unscaled coordinates

### Asset Loading
- **Image paths**: Use `os.path.join("ASSETS", filename)` pattern
- **Card images**: Follow `f"CARDS/{race}/{card_name}.png"` convention
- **UI scaling**: Use `scale_size()` for image dimensions, `scale_pos()` for positioning
- **Background scaling**: Backgrounds scale to `actual_width/actual_height` (full screen)

## Critical Dependencies & Setup

### Required Libraries
```bash
pip install pygame pygame_gui
```

### Key Globals
- `manager`: pygame_gui.UIManager instance using actual screen dimensions
- `screen`: Fullscreen pygame display using actual resolution
- `active_ui_elements`: Track all UI elements for cleanup
- `selected_cards`: Currently selected cards for gameplay
- `width/height`: Set to 1920/1080 for consistent positioning logic
- `actual_width/actual_height`: Real screen dimensions for display/backgrounds

### Common Debugging
- **Scaling issues**: Verify `scale_factor` calculation and helper function usage
- **UI positioning**: Check if using original 1920x1080 coordinates vs scaled coordinates
- **UI not appearing**: Check if elements added to `active_ui_elements`
- **Memory leaks**: Ensure `element.kill()` called before state changes
- **Card movement**: Verify `move_to()` uses original coordinates, not scaled ones
- **Asset loading**: Check file paths match exact ASSETS directory structure

## Development Workflows

### Adding New Cards
1. Define card in `declare_cards()` function
2. Add card image to `ASSETS/CARDS/[RACE]/`
3. Update race card arrays and `set_default_cards()`

### Creating New UI States
1. Add state to `game_state` conditional in main loop
2. Create `draw_[state]()` function using 1920x1080 coordinates
3. Handle state transitions in button event handlers
4. Ensure proper UI cleanup with `active_ui_elements.clear()`

### Resolution Testing
- Test with `scaling_demo.py` for visual verification
- Use `test_scaling.py` for coordinate calculation validation  
- Common test resolutions: 1366x768, 1280x720, 2560x1440, 3840x2160

### Asset Integration
- All UI buttons expect corresponding images in `ASSETS/BUTTONS/[SCREEN]/`
- Use `button.create_image()` after `button.create_box()` for visual buttons
- Background images automatically scale to full screen in `declare_images()`
- UI element images scale proportionally using `scale_size()` helper

## Game-Specific Logic

### Deck Building
- **20-card limit**: UI shows current deck size as "X/20"
- **Deck navigation**: `front_pointer`/`back_pointer` manage circular deck view
- **Profile system**: Switch between players with `current_profile` toggle

### Combat System
- **Energy costs**: Validate total energy before applying card effects
- **Health system**: Can go negative, ties decided by higher health
- **Turn timer**: 60-second countdown with automatic turn switch

### Data Flow
- **Card selection**: UI → `selected_cards` → `apply_card_effect()` → game state update
- **Player switching**: `switch_turn()` → `check_current_player()` → UI refresh
- **Game end**: Health check → winner determination → state change to `game_ended`
- **Coordinate flow**: Original 1920x1080 → automatic scaling → actual screen position