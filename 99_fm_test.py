import pyautogui
import time
fm = pyautogui.getWindowsWithTitle("Football Manager 2022")[0]
if fm.isActive == False: # open 'FM 2022'
    fm.activate()
#100,350 / 750,100
size = pyautogui.size()
pyautogui.click(100,350,duration=0.3) # click 'Training' 
pyautogui.click(750,100,duration=0.3) # click 'Individual' 
player_height = 270

pyautogui.click(500,player_height,duration=0.3)
praise_button_location = pyautogui.locateOnScreen("praise.png",confidence=0.95)
while praise_button_location :
    pyautogui.click(praise_button_location,duration=0.3) # click 'Praise'
    pyautogui.sleep(0.3)
    pyautogui.click(780,340,duration=0.2) # click 'put arm around'
    pyautogui.click(800,460,duration=0.2) # click ' first button of the praises'
    pyautogui.sleep(0.3)
    end_chat=pyautogui.locateOnScreen("end_chat.png",confidence=0.95) # find 'end-chat'
    pyautogui.click(end_chat,duration=0.2) # click 'end-chat'
    pyautogui.sleep(0.3)
    player_height+=57
    if player_height >= size[1]-40:
        break
    pyautogui.click(500,player_height,duration=0.5)
    

    
    
    
    
    

        



 
        
    







