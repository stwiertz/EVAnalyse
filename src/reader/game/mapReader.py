import cv2
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from src.reader.utils.ocrReader import OCRReader
def main(frame):
    mapFrame = frame[78:100, 825:1092]
    results = OCRReader.read_text(mapFrame)
    for (_, text, _) in results:
        if text is not None:
            text = text.replace(" ", "").replace("\n", "")
            if len(text) > 0:
                return text
    return None 


if __name__ == "__main__":
    image_path = './local/picture/frame_1.jpg'
    image = cv2.imread(image_path)
    
    result = main(image)
    print(f"Maps Name: '{result}'")