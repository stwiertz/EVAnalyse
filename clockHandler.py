import cv2 as cv 
import pytesseract
from pathlib import Path

ROOT_DIR = Path(__file__).parent
test_file = ROOT_DIR / './test.jpg'

def main():
    print("clockHandler")
    img = cv.imread(test_file)
    clockHandler(img, 1)
    # clockHandler(cv.imread("../src/result/Ceres/test.jpg"), 1)

def clockHandler(frame, frame_count):
    print("hello")
    # decoupage du timer
    clock = frame[ 0: 30, 930: 990]
    # passage au gris pour la lisibilite
    grayClock = cv.cvtColor(clock, cv.COLOR_BGR2GRAY)
    _, tresh = cv.threshold(grayClock, 150 , 255, cv.THRESH_BINARY_INV)    
    
    # extraction du text
    custom_config = r'--oem 3 --psm 6'
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    extractClock = pytesseract.image_to_string(tresh, config= custom_config)
    clockMinSec = extractClock.strip().split(':')
    if len(clockMinSec) < 2 or clockMinSec[0].isdigit() == False or  clockMinSec[1].isdigit() == False:
        print('error', clockMinSec)
        cv.imwrite("src/result/Ceres/start/error/{}.jpg".format(str(frame_count) + clockMinSec[0]), tresh)  
        return ;
    print(f"{clockMinSec[0]}:{clockMinSec[1]}")
    #test if the clock is detected correctly

if __name__ == "__main__":
    main()