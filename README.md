# Strategy Card Game  

**Developer:** [Ismael Rahman](https://www.linkedin.com/in/ismael-rahman-218428340/)  
**Sound Design:** Aadam  

---

## 📖 Overview  
This project is a **two-player, turn-based strategy card game** developed as part of my Computer Science NEA. The objective is to reduce the opponent’s health to zero using a variety of cards that feature different abilities, strategies, and playstyles.  

The game aims to balance **fun, accessibility, and strategy**, while still offering depth through different card types and tactical decision-making.  

---

## 🎮 Gameplay  
- Each player starts with **100 health** and **10 energy**.  
- A deck can contain **up to 20 cards**.  
- All 20 available cards are preloaded into each player’s deck to allow quick, strategic gameplay.  
- Health can drop below 0 without issues; if both players reach 0, the winner is the one with the higher remaining health (even if negative).  

---

## 🛠️ Features  
- Four distinct races with unique playstyles:  
  - **Humans:** Balanced and strategic  
  - **Elves:** Healing and tactical  
  - **Undead:** High damage, disposable, self-sacrificing  
  - **Dwarves:** Sturdy, strong damage, minor healing  
- Turn-based mechanics with **10 rounds**.  
- Energy-based system for card costs.  
- Sound design integrated for immersion.  

---

## 📂 Project Structure  
- `main.py` → Entry point of the game.  
- `ASSETS/` → Contains all images, buttons, and background visuals.  
- `SOUNDS/` → Contains music and sound effects.  
- `CARDS/` → Definitions and properties of all available cards.  

---

## 📦 Requirements  
This project is written in **Python** using **Pygame** and **pygame_gui**.  

Install required libraries with:  
```bash
pip install pygame pygame_gui
