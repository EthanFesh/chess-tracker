import chess
from vision_connector import VisionConnector

class ChessTracker:
    vision_connector : VisionConnector
    # Initialize python-chess board
    main_board = chess.Board()
    # Timing variables
    last_move_time = time.time()
    move_times = []

    def __init__(self):
        self.vision_connector = VisionConnector()

    def track_game(self, frame : np.ndarray) -> chess.Board:
        # TODO: Implement board transcription
        return None