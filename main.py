import pytesseract
import cv2
import pyautogui
import time
import os
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/Cellar/tesseract/5.1.0/bin/tesseract"

# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings
def clickItem(multi):
    pyautogui.moveTo(1400 / 2, (730 + multi + 10) / 2)
    pyautogui.click()
    pyautogui.moveTo(470,750)
    pyautogui.click()

def takeScreenshot(left, top, width, height,num: str):
    if(left == 1988):
        myScreenshot = pyautogui.screenshot(region=(left, top, width, height))
        myScreenshot.save('/Users/alecbyrd/PycharmProjects/bazaarfarmbot/images/graycheck.png')
        return myScreenshot
    else:
        myScreenshot = pyautogui.screenshot(region=(left, top, width, height))
        myScreenshot.save('/Users/alecbyrd/PycharmProjects/bazaarfarmbot/images/screenshot_'+ num + '.png')
        img = cv2.imread('images/screenshot_' + num + '.png')
        text = pytesseract.image_to_string(img)
        return text


def screenshotAllItems():
    goldPearlClickCount = 0
    bloodMossClickCount = 10
    sunstoneClickCount = 10
    ameCount = 1
    for x in range(10):
        multiplier = x*64

        text = takeScreenshot(1200,(730+multiplier),600,50,str(x))

        # if text.__contains__('GOLDEN PEARL'):
        #     clickItem(multiplier)
        #     for x in range(goldPearlClickCount):
        #         pyautogui.click(910,567)
        #         #ADD CLICK TO BUY
        #     pyautogui.moveTo(632,730)
        #     pyautogui.click()
        #     pyautogui.moveTo(920, 576)
        #     pyautogui.click()
        if text.__contains__('BLOOD MOSS'):
            clickItem(multiplier)
            for x in range(bloodMossClickCount):
                pyautogui.click(910,567)
                pyautogui.click()
                time.sleep(.5)
                pyautogui.moveTo(920, 576)
                pyautogui.click()
        elif text.__contains__('SUNSTONE'):
            clickItem(multiplier)
            for x in range(sunstoneClickCount):
                pyautogui.click(910,567)
            pyautogui.moveTo(632, 730)
            pyautogui.click()
            time.sleep(.5)
            pyautogui.moveTo(920, 576)
            pyautogui.click()
        elif text.__contains__('BRONZE GEAR'):
            clickItem(multiplier)
            for x in range(ameCount):
                pyautogui.click(910,567)
            pyautogui.moveTo(632, 730)
            pyautogui.click()
            time.sleep(.5)
            pyautogui.moveTo(920,576)
            pyautogui.click()
        print(text)



# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    time.sleep(3)
    pyautogui.moveTo(375, 282)
    pyautogui.click()
    rerun = 0
    while rerun != 1:
        screenshotAllItems()
        if pyautogui.pixelMatchesColor(1988,1420,(113,113,113)):
            pyautogui.moveTo(375,282)
            pyautogui.click()
            time.sleep(1)
            rerun+=1
        else:
            pyautogui.moveTo(994,710)
            pyautogui.click()
            for x in range(10):
                os.remove('images/screenshot_' + str(x) + '.png')

