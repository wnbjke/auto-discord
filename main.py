import pyautogui as py
import pyperclip
import time

"""
# IN CASE TO CHECK POSITION
pos = py.position()
print(pos.x, pos.y)
"""

# CONSTS
msg_x, msg_y = 1371, 491
user_x, user_y = 1624, 411
copy_btn_x, copy_btn_y = 1693, 332
gpt_x, gpt_y = 1541, 935
gpt_answer_x, gpt_answer_y = 1228, 828


def user_input():
    for i in range(200):
        time.sleep(1)
        # getting input
        py.moveTo(user_x, user_y)
        py.click(button="right")
        time.sleep(1)
        py.moveTo(copy_btn_x, copy_btn_y)
        py.click()
        copied_text_user = pyperclip.paste()
        print(f"Lenght of user text: {len(copied_text_user)}")
        print(copied_text_user)
        if "<" in copied_text_user:
            continue

        time.sleep(2)

        # pasting input to chat gpt
        py.moveTo(gpt_x, gpt_y)
        py.click()
        py.write(
            f"{copied_text_user}, answer only up to 5-7 words,in friendly format, with simple words")
        py.hotkey("enter")
        time.sleep(5)
        # getting answer from chat gpt
        py.moveTo(gpt_answer_x, gpt_answer_y)
        time.sleep(2)
        py.click(button="left", clicks=3, interval=0.1)
        time.sleep(2)
        # py.dragTo(gpt_answer_x, 0, button="left")
        py.hotkey("ctrl", "c")

        copied_text_answer = pyperclip.paste()

        # pasting response
        py.moveTo(msg_x, msg_y)
        py.click()

        py.write(copied_text_answer)
        py.hotkey("enter")


user_input()

'''
py.moveTo(msg_x, msg_y, 0.5)
py.click()
py.write("hello")
'''
