from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import keyboard
import time


cookies = webdriver.ChromeOptions()
cookies.add_argument(r"--user-data-dir=C:\Users\orlav\AppData\Local\Google\Chrome\User Data\Default")
cookies.add_argument(r'--profile-directory=Default')

chrome_browser = webdriver.Chrome(r'C:\Users\orlav\Desktop\chromedriver', options=cookies)
chrome_browser.get(r'https://web.whatsapp.com/')

print('We are in! Scanning Completed')

times = 3
chats = ['Bot0', 'Bot1', 'Bot2']
msgs = ['bla', 'bla bla', 'bla bla bla']

time.sleep(10)

while times > 0:
    for i in range(len(chats)):
        chat_name = chats[i]
        try:
            chat = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(chat_name))
            chat.click()
        except NoSuchElementException as e:
            search_bar = chrome_browser.find_element_by_xpath('//div[@class="_1awRl copyable-text selectable-text"]')
            search_bar.send_keys(chat_name + Keys.ENTER)
            time.sleep(3)

            chat = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(chat_name))
            chat.click()

        print('Chat Opened!')

        msg = msgs[i]

        txt_box = chrome_browser.find_element_by_xpath('//div[@class="DuUXI"]')
        txt_box.send_keys(msg + Keys.ENTER)
    times -= 1
    if keyboard.is_pressed('q'):
        break

print("Done")

if __name__ == '__main__':
    pass
