import cv2 as cv
import numpy as np
from time import time
from datetime import datetime
import pytesseract

from core.clockHandler import clockHandler

cap = cv.VideoCapture("./src/Phoenix_Ceres.mp4")
img = cv.imread("./core/dan.png")
cv.imshow("img", img )
cv.waitKey()
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Paramètres de l'OCR (ex. : langue anglaise, mode LSTM standard)


 # get frame rate 
# fps = cap.get(cv.CAP_PROP_FPS)
# print(f"le frame rarte de la video est :{fps} FPS")

loop_time = time()
frame_count = 0
startTime = datetime.now()
# potentiel soucis de fps sur le record

startMapTime = 60
currentTime : int = startMapTime
clockHandler(startMapTime ,1)

while False:

    ret, frame = cap.read()
    frame_count += 1
   
    # verifier si la video est terminer 
    if not ret:
        break

    # frame skipper
    if frame_count %60 != 0:
        # print("pass")
        continue
    # else: 
    #     print("no pass", frame_count, diff)
        

    # cv.putText(frame , str(diff), (70,70), cv.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2, cv.LINE_AA )
    # cv.putText(frame , str(round(frame_count/fps,2)), (70,100), cv.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2, cv.LINE_AA )

    ########
    # DETECTION du cronos
    ########
    
    # decoupage du timer
    clock = frame[ 0: 30, 930: 990]
    # passage au gris pour la lisibilite
    grayClock = cv.cvtColor(clock, cv.COLOR_BGR2GRAY)
    _, tresh = cv.threshold(grayClock, 150 , 255, cv.THRESH_BINARY_INV)    
    

    # extraction du text
    extractClock = pytesseract.image_to_string(tresh, config= custom_config)
    clockMinSec = extractClock.strip().split(':')
    # print('min', clockMinSec[0], " sec ", clockMinSec[1])
    if len(clockMinSec) < 2 or clockMinSec[0].isdigit() == False or  clockMinSec[1].isdigit() == False:
        print('error', clockMinSec)
        cv.imwrite("src/result/Ceres/start/error/{}.jpg".format(str(frame_count) + clockMinSec[0]), tresh)  
        continue 

    if (int(clockMinSec[0]) == 9 and int(clockMinSec[1]) > 50):
            currentTime = int(clockMinSec[1])
            print("ici")
            break
            # minimap = frame[23 : 240 , 10: 440]
            # cv.imwrite(f"src/result/start/Ceres/{clockMinSec[0] + "_" + clockMinSec[1] }.jpg", minimap)            
    
    loop_time = time()
    
    # key = cv.waitKey(1)
    # if key == ord('q'):
        
    #     cv.destroyAllWindows()
    #     break
    # elif key == ord("p"):
    #     cv.imwrite('src/recapscreen/positive/{}.jpg'.format(loop_time), frame)
    # elif key == ord("n"):
    #     cv.imwrite('src/recapscreen/negative/{}.jpg'.format(loop_time), frame)
    
diff = ( datetime.now() - startTime).seconds
print( "total time ", diff)
cap.release()