import numpy as np
import cv2

def get_hsv_range(hue, range_value, saturation_range=(100, 255), value_range=(100, 255)):
    # OpenCV uses H: 0-179, S: 0-255, V: 0-255
    hue_min = max(0, hue - range_value)
    hue_max = min(179, hue + range_value)
    
    # Create the lower and upper bounds
    lower = np.array([hue_min, saturation_range[0], value_range[0]])
    upper = np.array([hue_max, saturation_range[1], value_range[1]])
    
    return lower, upper

if __name__ == "__main__":        
        # Test the function with some example values
        hue = 60  # Yellow-green hue
        range_value = 10
        
        lower, upper = get_hsv_range(hue, range_value)
        
        print(f"Target hue: {hue}")
        print(f"Lower HSV bound: {lower}")
        print(f"Upper HSV bound: {upper}")
        
        # Optional: Create a simple visualization
        hsv_color = np.uint8([[[hue, 200, 200]]])
        rgb_color = cv2.cvtColor(hsv_color, cv2.COLOR_HSV2BGR)
        
        print(f"Corresponding BGR color: {rgb_color[0][0]}")