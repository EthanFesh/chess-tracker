import time
import chess
import chess.pgn
import numpy as np
from typing import Optional
from .vision_connector import VisionConnector
from app.utils import vision_connector

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
        self.last_detected_move = None
        self.last_move_detected_time = None
    
    def __del__(self):
        if hasattr(self, 'vision_connector') and self.vision_connector is not None:
            self.vision_connector.release_camera()

    def process_frame(self):
        """
        Processes a single frame from the vision system, detects moves, and updates the board state.
        """
        frame = self.vision_connector.get_frame()
        curr_board = self.frame_to_board(frame)
        move = self.get_move(curr_board)
        if move and move is not self.last_detected_move:
            self.last_move_detected_time = time.time()
            self.last_detected_move = move

        if (
            self.last_move_detected_time is not None and
            time.time() - self.last_move_detected_time >= 500
        ):
        
            self.board = self.update_board(move)
            
            self.last_move_detected_time = None
            self.last_detected_move = None

    def frame_to_board(self, frame):
        """
        Converts a frame to a chess.Board object. (Stub implementation)
        """
        # TODO: Implement actual vision-to-board logic
        return self.board.copy()

    def get_move(self, board2):
        board1 = self.board

        move = None
        for candidate in board1.legal_moves:
            board1_copy = board1.copy()
            board1_copy.push(candidate)
            if board1_copy.board_fen() == board2.board_fen():
                move = candidate
                break

        if move is not None:
            print(f"The move is: {move.uci()}")
            return move
        else:
            # print("No move was made yet.")
            return None

    def update_board(self, move):
        """
        Updates the internal board state with the given move and records move timing.
        """
        self.board.push(move)
        now = time.time()
        move_time = now - self.last_move_time
        self.move_times.append(move_time)
        self.last_move_time = now
        return self.board

    def is_valid_move(self, previous_board, current_board) -> bool:
        """
        Determines if only one valid move has been made between two board states.
        Returns True if the move is valid, False otherwise.
        """
        return True

    

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
        