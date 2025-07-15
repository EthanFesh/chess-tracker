# Chess Tracker

Chess Tracker is a Python application that uses your computer or phone camera to watch a live chess match, automatically detect moves, and generate a digital twin of the game in real time. It leverages computer vision (OpenCV) for board and piece detection, and uses the python-chess library for move validation, board state management, and PGN (Portable Game Notation) generation.

## Features
- Live camera input to monitor a physical chessboard
- Automatic move detection and validation
- Real-time digital board update and PGN generation
- Tracks the amount of time each player takes to move
- Designed for easy extension and experimentation

## Core Technologies
- [python-chess](https://python-chess.readthedocs.io/en/latest/): For chess logic, move validation, and PGN handling
- OpenCV: For camera access and image processing
- Python 3.8+

## Project Structure
- `chess-tracker/track_game.py`: Main script for running the chess tracker
- `pyproject.toml`, `poetry.lock`: Dependency management files

## Installation

1. **Install Poetry** (if you don't have it):
   ```sh
   curl -sSL https://install.python-poetry.org | python3 -
   # Or see https://python-poetry.org/docs/#installation for details
   ```
2. **Install dependencies:**
   ```sh
   poetry install
   ```

## Getting Started
1. Make sure your camera is connected and accessible.
2. Run the main script using Poetry:
   ```sh
   poetry run python chess-tracker/track_game.py
   ```
3. Point your camera at a chessboard and start playing!

## Basic Usage

- **Run the tracker:**
  ```sh
  poetry run python chess-tracker/track_game.py
  ```
- To add new dependencies, use:
  ```sh
  poetry add <package-name>
  ```

## TODO
- Implement board and piece detection logic
- Improve move recognition accuracy
- Add user interface for corrections and game export
