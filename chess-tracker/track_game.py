from typing import final
import cv2
import chess
import time
from chess_tracker import ChessTracker

chess_tracker : ChessTracker

def main():
    chess_tracker = ChessTracker()
    chess_tracker.track_game(cap)

if __name__ == "__main__":
    main()