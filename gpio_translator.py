import logging
from pyautogui import press
from gpiozero import Button

import sys

#https://gpiozero.readthedocs.io/en/stable/api_input.html

def gpio_translate ():

    try:
        #GPIO Pins: 5, 6, 13, 19, 26
        button_left = Button(5)
        button_right = Button(6)
        button_up = Button(13)
        button_down = Button(19)
        button_enter = Button(26)
    except:
        logging.warn('GPIO Transl.: No GPIO found')
        sys.exit()

    buttons = []
    buttons.append(button_left)
    buttons.append(button_right)
    buttons.append(button_up)
    buttons.append(button_down)
    buttons.append(button_enter)

    #Button config
    for button in buttons:
        button.hold_repeat=False
        button.hold_time=0

    while True:
        if button_left.is_held:
            press ('left')
            logging.info('GPIO Transl.: Left')
        
        if button_right.is_held:
            press ('right')
            logging.info('GPIO Transl.: Right')
        
        if button_up.is_held:
            press ('up')
            logging.info('GPIO Transl.: Up')

        if button_down.is_held:
            press ('down')
            logging.info('GPIO Transl.: Down')

        if button_enter.is_held:
            press ('enter')
            logging.info('GPIO Transl.: Enter')

        