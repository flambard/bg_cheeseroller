import pyautogui
import pytesseract
from datetime import datetime
import time

total_roll_relpos = (144, 400, 40, 32)
store_button_relpos = (-86, 465)
reroll_button_relpos = (216, 465)

def store_roll(x, y):
    relx, rely = store_button_relpos
    pyautogui.moveTo(x+relx, y+rely)
    pyautogui.mouseDown()
    time.sleep(0.2)
    pyautogui.mouseUp()

def reroll(x, y):
    relx, rely = reroll_button_relpos
    pyautogui.click(x = x+relx, y = y+rely)

def scan_roll(x, y):
    relx, rely, width, height = total_roll_relpos
    return pyautogui.screenshot(region=(x+relx, y+rely, width, height))



max_roll = 108

print ("Max roll:", max_roll)

# Locate the "Abilities" headline
headline_x, headline_y, _width, _height = pyautogui.locateOnScreen("headline_image.ppm")

print ("Headline location:", headline_x, headline_y)

start_time = datetime.now()
print ("Starting time:", start_time)

best_roll = 0
roll_count = 1

while(best_roll < max_roll):
    roll_image = scan_roll(headline_x, headline_y)
    roll_text = pytesseract.image_to_string(roll_image)
    current_roll = int(roll_text)

    if current_roll > best_roll:
        store_roll(headline_x, headline_y)
        print ("New best:", current_roll, "rolled after", datetime.now() - start_time)
        best_roll = current_roll

    roll_count += 1
    reroll(headline_x, headline_y)


completed_time = datetime.now()
print ("Completed at:", completed_time)
print ("Time spent:", completed_time - start_time)
print ("Roll count:", roll_count)
