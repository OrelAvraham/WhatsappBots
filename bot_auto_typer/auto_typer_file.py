import pyautogui
import keyboard
import time

'''
Hardcoded Auto Typer Instructions:
    The auto typer is a bot that simulates typing the msg
    The file version interacts with the user through the info.txt file. The user will write the needed
    information in a format you can see in the info file

    Keyword variables:
    sleep_time -- the time the code will wait after starting it till it will start typing, in seconds (int)
    msg -- the message the bot will type (string)
    times -- the times that the bot will spam (if times is not positive the bot will span until you press 'q')
'''

with open('info.txt', 'r') as f:
    data = f.read()
    data = data.split('\n')

    sleep_time = int(data[0].split(' ')[1])
    times = int(data[1].split(' ')[1])
    data = data[2:]
    msg = str(' ').join(data)

time.sleep(sleep_time)

if times > 0:
    for i in range(times):
        pyautogui.typewrite(msg)
        pyautogui.press("enter")
        print(msg)
else:
    while 1:
        if keyboard.is_pressed("q"):
            break
        pyautogui.typewrite(msg)
        pyautogui.press("enter")

if __name__ == '__main__':
    pass
