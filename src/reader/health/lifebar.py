import cv2
import numpy as np
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from src.reader.utils.hsv_range import get_hsv_range
from src.reader.utils.color import ORANGE_HSV, BLEU_HSV

def main(frame, yTpl =(732, 735), xTpl=(32, 391), isOrange=True):
    # Extract lifebar region
    lifebarFrame = frame[yTpl[0]:yTpl[1], xTpl[0]:xTpl[1]]
    
    # Convert to HSV for better color analysis
    hsv_frame = cv2.cvtColor(lifebarFrame, cv2.COLOR_BGR2HSV)
    
    # Get the first row of pixels
    first_row = hsv_frame[1, :]
    
    # Print every 10th value to keep log manageable
    print("HSV values from right to left (every 10th pixel):")
    step = int((xTpl[1] - xTpl[0]) / 10)
    for i, hsv_pixel in enumerate(first_row):
        if i % step == 0 or i ==  len(first_row) - 1:
            h, s, v = hsv_pixel
            if  (isOrange and 200 < v < 255) or (not isOrange and 0 < v < 200):
                print(f"{i/step}HP Pixel {i}: H={h}, S={s}, V={v}, IS ALIVE")
            else:
                return 0 if isOrange else 100
    
    
    return 100 if isOrange else 0

if __name__ == "__main__":
    image_path = './local/picture/frame_1.jpg'
    image_path_2 = './local/picture/frame_2580_aka_mort.jpg'
    image = cv2.imread(image_path_2)
    
    if image is None:
        print(f"Error: Could not read image from {image_path}")
    else:
        hp = main(image)
        print(f"lifebar: Hp={hp}")
