import pyautogui
import keyboard
import time

'''
Hardcoded Auto Typer Instructions:
    The auto typer is a bot that simulates typing the msg
    The console version interacts with the user through the console. The user will be asked 
    to what value he wants to set the variables.

    Keyword variables:
    sleep_time -- the time the code will wait after starting it till it will start typing, in seconds (int)
    msg -- the message the bot will type (string)
    times -- the times that the bot will spam (if times is not positive the bot will span until you press 'q')
'''

sleep_time = int(input('Enter the sleep time: '))
msg = input('Enter the message: ')
times = int(input('Enter the times you want the bot to send the messages: '))
time.sleep(sleep_time)

if times > 0:
    for i in range(times):
        pyautogui.typewrite(msg)
        pyautogui.press("enter")
else:
    while 1:
        if keyboard.is_pressed("q"):
            break
        pyautogui.typewrite(msg)
        pyautogui.press("enter")

if __name__ == '__main__':
    pass
