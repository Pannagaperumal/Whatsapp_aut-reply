import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(3)

position1 = pt.locateOnScreen("smiley.png", confidence=.6)
x = position1[0]
print(x)
y = position1[1]
print(y)
#gets message
def get_message():
    global x,y

    postion= pt.locateOnScreen("smiley.png", confidence=.6)
    x = position1[0]
    y = position1[1]
    pt.moveTo(x,y, duration=.05)
    pt.moveTo(x + 70, y - 40, duration = .5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("message received: " + whatsapp_message)

    return whatsapp_message

#posts
def post_response(message):
    global x, y

    position = pt.locateOnScreen("smiley.png", confidence=.6)
    x = position1[0]
    y = position1[1]
    pt.moveTo(x + 200, y + 20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01)

    pt.typewrite("\n", interval=.01)

#process response
def process_response(message):
    random_no = random.randrange(3)
    if "?"in str(message).lower():
        return "Oh i see, I'll let him know about it - Pannu's Bot"

    else: 
        if "hi" or "hey" or "oi" in str(message).lower():
            return "Hey,whatsup.\n - Pannu's Bot"
        elif "happy new year"in str(message).lower():
            return "Wishing you and your family a very Happy New Year! ✨\n -Pannu's Bot "
        elif "good morning"in str(message).lower():
            return"Good Morning! \n -Pannu's Bot"
        elif "good night"in str(message).lower():
            return"Good Night! Sleep tight"
        elif "hello":
            return "Hello! How can i help you\n -Pannu's bot"
        else:
            return"hey!"   


#new messages check
def check_for_new_messages():
    pt.moveTo(x + 50, y - 45, duration=.5)

    while True:
        try:
            position = pt.locateOnScreen("circle.png", confidence = .7)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                processed_message = process_response(get_message())
                post_response(processed_message)
                sleep(10)

            else:
                print("No messages")
                sleep(10)

        except(Exception):
            print("No new messages")
#processed_message = process_response(get_message())
#post_response(processed_message)
check_for_new_messages()
