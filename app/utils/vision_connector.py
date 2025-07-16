import cv2
import numpy as np
import logging
import time
from typing import Optional


class VisionConnector:
    """
    This class is responsible for interacting with your camera
    to capture frames
    """

    camera: cv2.VideoCapture
    current_frame: Optional[np.ndarray]
    last_frame_time: float
    frame_interval: float

    def __init__(self, fps: float = 10):
        self.camera = cv2.VideoCapture(0)
        self.current_frame = None
        self.last_frame_time = 0.0
        self.frame_interval = 1.0 / fps
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def get_frame(self) -> Optional[np.ndarray]:
        """
        Returns the current frame, respecting the object's FPS setting.
        Only grabs a new frame from the camera if enough time has passed since the last frame;
        otherwise, returns the cached frame. If the camera fails to provide a frame, returns None.
        """
        now = time.time()
        if self.current_frame is None or (now - self.last_frame_time) >= self.frame_interval:
            successful, frame = self.camera.read()
            if not successful:
                self.logger.error("Failed to grab frame from camera.")
                return None
            self.current_frame = frame
            self.last_frame_time = now
        else:
            self.logger.debug("Returning cached frame.")
        return self.current_frame

    def release_camera(self):
        """
        Releases the camera resource when done.
        """
        if self.camera is not None:
            self.camera.release()
            print("Camera released.")
        