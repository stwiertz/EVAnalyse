import cv2
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from src.reader.health.lifebar import main as lifebar
from src.core.Player import Player


def main(frame, debugger=None):
    player_one = Player(healthbar= ((732, 735), (32, 391)), isOrange =True)
    hp = lifebar(frame, player_one.getHealthBar(), True)
    player_one.setHealth(hp)
    if debugger:
        debugger.addText(f"Hp={hp}",coordinates = (391, 745))
    
    player_two = Player(healthbar= ((815, 820), (32, 391)), isOrange =True)
    hp = lifebar(frame, player_two.getHealthBar(), True)
    player_two.setHealth(hp)
    if debugger:
        debugger.addText(f"Hp={hp}",coordinates = (391, 860))


if __name__ == "__main__":
    image_path = './local/picture/frame_1.jpg'
    frame = cv2.imread(image_path)
    main(frame)