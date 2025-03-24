import easyocr
import cv2

# Initialize the reader globally
reader = easyocr.Reader(['en'], gpu=True)  # Enable CUDA by setting gpu=True

def main(frame):
    if frame is None:
        raise ValueError("Error: Frame is None.")
    timerFrame = frame[0:28, 934:986]
    results = reader.readtext(timerFrame)  # Use the globally initialized reader
    for (bbox, text, prob) in results:
        return text

if __name__ == "__main__":
    image_path = './local/picture/frame_1.jpg'
    image = cv2.imread(image_path)

    print(f"Timer: '{main(image)}'")