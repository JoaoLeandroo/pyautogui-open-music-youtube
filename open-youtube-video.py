import pyautogui

pyautogui.hotkey("win", "r")
pyautogui.sleep(1)
pyautogui.press("enter")
pyautogui.sleep(1)


pyautogui.write("cd ..")
pyautogui.sleep(0.5)
pyautogui.press("enter")
pyautogui.write("cd ..")
pyautogui.sleep(0.5)
pyautogui.press("enter")
pyautogui.sleep(0.5)
pyautogui.write("cd ProgramData\Microsoft\Windows\Start Menu\Programs")
pyautogui.sleep(0.5)
pyautogui.press("enter")
pyautogui.sleep(0.5)

pyautogui.write('start "" "Google Chrome" ')
pyautogui.sleep(0.5)
pyautogui.press("enter")
pyautogui.sleep(1)

pyautogui.write("https://www.youtube.com/")
pyautogui.sleep(1)
pyautogui.press("enter")
pyautogui.sleep(2)

pyautogui.click(920,144, duration=0.5)
pyautogui.sleep(0.5)

pyautogui.write("avicii the nights")
pyautogui.sleep(0.5)
pyautogui.press("enter")
pyautogui.sleep(2)

pyautogui.click(693,448, duration=0.5)


