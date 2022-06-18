import pytesseract
import cv2
import pyautogui
import time
import os
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/Cellar/tesseract/5.1.0/bin/tesseract"

# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings
def clickItem(multi):
    """
    Clicks the item inputted as a parameter
    :param multi: the current multiplier of the screenshot
    :return: void
    """
    pyautogui.moveTo(1400 / 2, (730 + multi + 10) / 2)
    pyautogui.click()
    pyautogui.moveTo(470,750)
    pyautogui.click()

def takeScreenshot(left, top, width, height,num: str):
    """
    Screenshots with the given parameters, then returns the text that was in the image
    :param left: left bound
    :param top: top bound
    :param width:
    :param height:
    :param num: current screenshot #
    :return: text that was in the image
"""
    myScreenshot = pyautogui.screenshot(region=(left, top, width, height))
    myScreenshot.save('/Users/alecbyrd/PycharmProjects/bazaarfarmbot/images/screenshot_'+ num + '.png')
    img = cv2.imread('images/screenshot_' + num + '.png')
    text = pytesseract.image_to_string(img)
    return text

def checkItem(count: int, item: str, position: int, text):
    """
    Checks an item to see if it is one that needs to be bought or not
    :param count: How many to buy total
    :param item: What item to buy
    :param position: Current position of the item that is to be bought
    :param text: the string that was gotten from the image
    :return:
    """

    if text.__contains__(item):
        #selects item to buy
        clickItem(position)

        #cliks arrow button
        pyautogui.moveTo(920, 576)
        for x in range(count-1):
            pyautogui.click()

        #clicks buy
        pyautogui.moveTo(640,730)
        pyautogui.click()

        time.sleep(.5)
        #clicks confirmation message
        pyautogui.moveTo(900,575)
        pyautogui.click()

        time.sleep(.5)

def screenshotAllItems():
    """
    Screenshots all items, and checks all of the items
    :return: None
    """
    items = ('BLOOD MOSS', 10), ('SUNS TONE', 10), ('BRONZE GEAR', 1)
    for x in range(10):
        multiplier = x*64
        text = takeScreenshot(1200,(730+multiplier),600,50,str(x))
        for item in items:
            checkItem(item[1],item[0],multiplier,text)
        print(text)

if __name__ == '__main__':
    #wait 3 seconds to start
    time.sleep(3)

    #resets the bazaar
    pyautogui.moveTo(375, 282)
    pyautogui.click()


    rerun = 0
    while rerun != 3: # Number of time it reruns until stopping

        #Goes through all items on the page
        screenshotAllItems()

        # If the arrow is gray, then reset the bazaar
        if pyautogui.pixelMatchesColor(1994, 1418, (113, 113, 113), tolerance=10):
            pyautogui.moveTo(375,282)
            pyautogui.click()
            rerun += 1
            time.sleep(1)

        # If the arrow is green then go to the next bazaar page
        else:
            pyautogui.moveTo(994,710)
            pyautogui.click()
            #deletes the screenshots that were taken
            for x in range(10):
                os.remove('images/screenshot_' + str(x) + '.png')
