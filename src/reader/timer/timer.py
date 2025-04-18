import cv2
import re
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from src.reader.utils.ocrReader import OCRReader

# Initialize the reader globally


def main(frame):
    if frame is None:
        raise ValueError("Error: Frame is None.")
    
    timerFrame = frame[0:28, 934:986]
    results = OCRReader.read_text(timerFrame)
    
    for (_, text, _) in results:
        # Extract only digits from the text
        digits = re.findall(r'\d', text)
        
        # If we have at least 4 digits, take first 2 as minutes and last 2 as seconds
        if len(digits) >= 4:
            minutes = ''.join(digits[:2])
            seconds = ''.join(digits[-2:])
            return f"{minutes}.{seconds}"
        
        # If we have exactly 3 digits, assume format is M.SS or MM.S
        elif len(digits) == 3:
            minutes = digits[0]
            seconds = ''.join(digits[1:])
            return f"0{minutes}.{seconds}"
        
        # If we have only 1 or 2 digits, assume these are seconds only
        elif len(digits) > 0:
            seconds = ''.join(digits)
            if len(seconds) == 1:
                seconds = "0" + seconds
            return f"00.{seconds}"
    
    # Default return if no text was found or processed
    return "00.00"

if __name__ == "__main__":
    image_path = './local/picture/frame_1.jpg'
    image = cv2.imread(image_path)
    
    result = main(image)
    print(f"Timer: '{result}'")