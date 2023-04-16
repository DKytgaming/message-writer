import pyautogui as p
import time as t

msg=input("Enter the message you want to spam: ")
no=int(input("Enter how many times you want spam the message: "))

thi.sleep(3)

for i in range(no):
    p.typewrite(msg)
    p.press('Enter')


#Made by DKytgaming 
#Github - https://github.com/DKytgaming
