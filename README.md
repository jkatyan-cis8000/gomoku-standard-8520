# gomoku-standard-8520
A standard 15x15 Gomoku game implementation where two players alternate placing black and white stones to form an unbroken line of five.

## Files
- `core.py` - Core game logic (board state, move validation, win detection)
- `ui.py` - Console UI (board display, input handling, game loop)
- `main.py` - Entry point

## How to Play
```bash
python3 main.py
```

## Game Rules
- Players take turns placing stones on a 15x15 grid
- Black plays first, then white alternates
- First player to get 5 stones in a row (horizontal, vertical, or diagonal) wins
- If the board fills without a winner, the game is a draw
