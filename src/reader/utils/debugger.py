import cv2

class Debugger:

    def __init__(self):
        self.debug = False
        self.texts = []

    def addText(self, text,coordinates=(0, 0), color=(0, 255, 0), scale=0.7, thickness=2):
        self.texts.append((text, coordinates, color, scale, thickness))

    def addToFrame(self, frame):
        cv2.putText(frame, f"Debug {len(self.texts)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        for text, coordinates, color, font_scale, thickness in self.texts:
            cv2.putText(frame, text, coordinates, cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, thickness)
        return frame