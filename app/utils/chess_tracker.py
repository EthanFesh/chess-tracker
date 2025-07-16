import time
import chess
import chess.pgn
import numpy as np
from typing import Optional
from vision_connector import VisionConnector

class ChessTracker:
    """
    ChessTracker is the main class responsible for managing a chess game session.
    It integrates the vision system for board state detection, maintains the digital chess board,
    tracks move times, and provides methods to validate and track the game state.
    """
    vision_connector: VisionConnector  # The vision connector to use
    board: chess.Board  # The digital twin of the real game
    last_move_time: float  # The time of the last move
    move_times: list[float]  # The times of consecutive moves

    def __init__(self, fps: float):
        self.vision_connector = VisionConnector(fps)
        self.board = chess.Board()
        self.last_move_time = time.time()
        self.move_times = []
    
    def __del__(self):
        if hasattr(self, 'vision_connector') and self.vision_connector is not None:
            self.vision_connector.release_camera()

    def process_frame(self, frame: Optional[np.ndarray]):
        """
        Processes a single frame from the vision system, detects moves, and updates the board state.
        """
        pass

    def is_valid_move(self, previous_board, current_board) -> bool:
        """
        Determines if only one valid move has been made between two board states.
        Returns True if the move is valid, False otherwise.
        """
        return True

    def update_board(self, move):
        """
        Updates the internal board state with the given move and records move timing.
        """
        pass

    def export_pgn(self):
        """
        Exports the current game to a PGN file using the python-chess library.
        """
        filename = input("Enter game name: ")
        game = chess.pgn.Game.from_board(self.board)
        with open(filename, "w", encoding="utf-8") as pgn_file:
            exporter = chess.pgn.FileExporter(pgn_file)
            game.accept(exporter)
        print(f"Game exported to {filename}")
        