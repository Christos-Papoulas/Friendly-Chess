# Friendly-Chess
It's a friendly chess because it finds all unique combinations of a set of chess pieces on a chess board with size S where none of the pieces is in a position to take any of the others.

### How to run the Friendly-Chess
Just: `python chess.py`

The friendly chess can be configured with:
```
[chess]
size = 3
pieces = K K R
```
accepted pieces: K, Q, B, R, N

### How it works
It's an recursive brute-force algorithm.
It tries to find a solution board. When it finds one, then it rotates the board by 90, 180 and 260 degrees, if those new solutions aren't in the already found solutions then it adds them. 