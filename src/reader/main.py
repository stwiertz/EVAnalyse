import cv2
import time
from timer.timer import main as timer

def main(path):

    cap = cv2.VideoCapture(path)

    print("R ==> this is the reader", path)
    if not cap.isOpened():
        print(f"Error: Could not open video file {path}")
        return

    count = 0
    framskip = 60
    start_time = time.time()
    sec = 0
    while True:
        ret, frame = cap.read()
        count += 1
        if not ret:
            print("End of video or error reading frame.")
            break
        if count % framskip != 0:
            #print(f"Frame {count} read successfully")
            continue
        
        # Timer
        print(f"Timer {timer(frame)}")
        
        #Frame exporter
        if sec == 60:
            #output_path = f"./local/picture/frame_{count}.jpg"
            #cv2.imwrite(output_path, frame)
            print(f"Frame {count} read successfully")
        
        # Press 'q' to exit
        #if cv2.waitKey(25) & 0xFF == ord('q'):
            #break
        
        if(count % (framskip * 100) == 100):
            print(f"Frame {count} read successfully")
             
    
    end_time = time.time()  # End timing
    elapsed_time = end_time - start_time  # Calculate elapsed time
    print('Count', count)
    print(f"Time taken by the while loop: {elapsed_time:.2f} seconds")


    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main('./local/video/arte.mp4')
