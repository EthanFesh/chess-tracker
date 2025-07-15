from typing import final
import cv2
import chess
import time

# Initialize camera (default camera index 0)
cap = cv2.VideoCapture(0)

# Initialize python-chess board
main_board = chess.Board()

# Timing variables
last_move_time = time.time()
move_times = []

# Placeholder for previous board state (to be implemented)
previous_board_state = None
current_board_state = None

def main():
    while True:
        try:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame from camera.")
                break

            # TODO: create a new board state
            current_board_state = main_board.copy()

            # TODO: Detect move from frame
            detected_move = detect_move_from_frame(frame, previous_board_state)

            if is_new_board_state(current_board_state, previous_board_state):
                # TODO: push the move to the board
                main_board.push(detected_move)
                # TODO: update the previous board state
                previous_board_state = current_board_state
                # TODO: update the move times
                move_times.append(time.time() - last_move_time)
            
           
        except Exception as e:
            print(f"Error: {e}")
            continue

        finally:
            cv2.imshow('Chess Tracker', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        

def detect_move_from_frame(frame, previous_board_state):
    """
    Placeholder function to detect a move from the current frame and previous board state.
    Should return a UCI string (e.g., 'e2e4') if a move is detected, else None.
    """
    # TODO: Implement board and piece detection logic
    return None

if __name__ == "__main__":
    main()