
# 🚨 Crazy Robber 🚨

**Crazy Robber** is an exciting 2D game where you control a clever robber navigating through a maze-like city, avoiding watchmen, collecting treasures, and escaping safely. The game features dynamic obstacles, increasing difficulty, and a score-based system.

---

## 🛠️ **Features**

✅ Smooth and interactive player movement.  
✅ Randomly moving watchmen as dynamic obstacles.  
✅ Collectible treasures to increase the score.  
✅ Collision detection with police cars and boundaries.  
✅ Game over screen with final score and replay option.  
✅ Clean and modular code structure.

---

## 🎮 **How to Play**

1. **Move the Robber:** Use the arrow keys (`↑`, `↓`, `←`, `→`) to move the robber across the map.
2. **Avoid Watchmen:** Dodge the watchmen moving randomly on the screen.
3. **Collect Treasures:** Pick up treasures to increase your score.
4. **Escape or Survive:** The goal is to collect as many treasures as possible while avoiding the police.

---

## 🖥️ **Installation and Execution**

1. **Clone the repository:**
   ```bash
   git clone <repository-link>
   cd crazy-robber
   ```

2. **Install dependencies:**
   Make sure you have `pygame` installed. If not, install it using:
   ```bash
   pip install pygame
   ```

3. **Run the game:**
   ```bash
   python main.py
   ```

---

## 📦 **Folder Structure**

```
/crazy-robber
 ├── assets/              # Contains images, sounds, and game assets
 ├── main.py              # Entry point of the game
 ├── game.py              # All components of game are assembled here
 ├── pathfinding.py       # Algorithms used like bfs and a star 
 ├── robber.py            # Player character (robber) logic
 ├── watchman.py          # Police car (dynamic obstacle) logic
 ├── coin.py              # Treasure collectible logic
 ├── utils.py             # Helper functions
 ├── constants.py         # Game config
 ├── wall.py              # Static obstacles
 ├── grid.py              # Grid login
 ├── metrics.py           # Game analysis logic
 ├── README.md            # Project documentation
 └── requirements.txt     # List of dependencies
```

---

## 🛠️ **Technologies Used**

- Python 🐍  
- Pygame 🎮  
- Object-oriented programming (OOP) principles  

---

## 🚀 **Future Improvements**

- ✅ Add more challenging levels with different city layouts.  
- ✅ Introduce power-ups for temporary invincibility or speed boosts.  
- ✅ Include a main menu and settings screen.  
- ✅ Add sound effects and background music.  

---

## 📝 **License**

This project is licensed under the MIT License.  
Feel free to modify and enhance it as you like! 🎉
