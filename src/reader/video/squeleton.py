import cv2
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from src.reader.game.mapReader import main as mapReader
from src.reader.timer.timer import main as timerReader

def main(cap):
    total_Frame =cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    current_frame_count = 0
    time_step = 30 * fps
    previous_map = None
    inprogress = False

    while True:
        cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame_count-1)
        ret, frame = cap.read()
        if not ret:
            break
        current_map = mapReader(frame)
        if current_map is None:
            current_frame_count += time_step
            continue
        current_timer = timerReader(frame)
        minutes, seconds = current_timer.split(".")
        if previous_map is None or current_map != previous_map:
            if current_timer != "10.00":
                previous_map = current_map
                temp_time = int(current_frame_count / fps) + int(int(minutes) * 60 + int(seconds)) - 10 *60 
                vid_minutes = int(temp_time/60)
                vid_seconds = int(temp_time % 60)
                print(f"Maps Name: '{current_map}', Start at : '{vid_minutes:02d}:{vid_seconds:02d}'")
            
        current_frame_count += time_step
    pass

if __name__ == "__main__":
    cap = cv2.VideoCapture('./local/video/250206_secret_frozen.mp4')  
    #cap = cv2.VideoCapture('./local/video/arte.mp4')

    main(cap)