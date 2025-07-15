# This file is intended to be used to transcribe the board from a frame
# It will take in a frame and return a board state
# It will use the chess library to transcribe the board
# It will return a board state that can be used to track the game

import chess

# 
class VisionConnector:
    # Initialize camera (default camera index 0)
    cap = cv2.VideoCapture(0)