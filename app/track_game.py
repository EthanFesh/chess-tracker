import time
from .utils.chess_tracker import ChessTracker

def main():
    print("Welcome to the chess tracker, enjoy!")
    fps = float(input("Enter desired FPS: "))
    chess_tracker = ChessTracker(fps)
    
    while True:
        try:
            frame = chess_tracker.vision_connector.get_frame()
            if frame is not None:
                chess_tracker.process_frame(frame)
            else:
                print("No frame received")
        except KeyboardInterrupt:
            # User pressed Ctrl+C, show the menu
            action = handle_user_input()
            if action == 'quit':
                print("Exiting Chess Tracker. Goodbye!")
                break
            elif action == 'pause':
                print("Resuming...")
                continue
            elif action == 'export':
                chess_tracker.export_pgn()
                continue

def handle_user_input():
    print("Enter command: [q]uit, [p]ause, [e]xport PGN, or press Enter to continue.")
    command = input().strip().lower()
    if command == 'q':
        print("Quitting the game.")
        return 'quit'
    elif command == 'p':
        print("Game paused. Press Enter to continue.")
        input()
        return 'pause'
    elif command == 'e':
        print("Exporting game to PGN.")
        return 'export'
    else:
        return None

if __name__ == "__main__":
    main()