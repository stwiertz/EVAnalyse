import cv2
import time
from timer.timer import main as timer
from health.lifebar import main as lifebar

# Mouse callback function
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # Left mouse button clicked
        # Convert coordinates from display frame to original frame
        scale_factor = param['scale_factor']
        original_x = int(x / scale_factor)
        original_y = int(y / scale_factor)
        
        print(f"Clicked at: ({original_x}, {original_y})")

def main(path):
    cap = cv2.VideoCapture(path)

    print("R ==> this is the reader", path)
    if not cap.isOpened():
        print(f"Error: Could not open video file {path}")
        return

    # Scale factor for display
    scale_factor = 0.8
    
    # Set mouse callback
    cv2.namedWindow('Frame')
    param = {'scale_factor': scale_factor}
    cv2.setMouseCallback('Frame', click_event, param)

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
        timer_value = timer(frame)
        
        #Frame exporter
        if count == 2580:
            output_path = f"./local/picture/frame_{count}_aka_mort.jpg"
            cv2.imwrite(output_path, frame)
            print(f"Frame {count} read successfully")
        
        # Draw rectangle around timer region
        cv2.rectangle(frame, (32, 730), (391, 733), (0, 255, 0), 2)
        
        # Resize frame for display
        display_width = int(frame.shape[1] * scale_factor)
        display_height = int(frame.shape[0] * scale_factor)
        display_frame = cv2.resize(frame, (display_width, display_height))
        
        # Display the resized frame
        cv2.imshow('Frame', display_frame)
        
        # Press 'q' to exit
        if cv2.waitKey(10) & 0xFF == ord('q'):
            print(f"Exiting... {count} frames processed {timer_value}")
            break

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
