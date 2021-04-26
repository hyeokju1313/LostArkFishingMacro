import os
import time
import sys
import pyautogui as pa
import configparser

# - 주모니터의 화면의 Center 를 Return -
def getCenterOfScreen():
    tup = pa.size()
    tup = (int(tup[0]/2), int(tup[1]/2))
    return tup

# - 느낌표를 검출할 영역을 지정 -
def makeRegion(center, width, height):
    x = center[0]
    y = center[1]
    startPos = (x - width, y - height)
    region = (startPos[0], startPos[1], 2*width, 2*height)
    return region

# - 이미지 File이름, 검출 대상이 될 영역을 입력받아 이미지를 검출하는 함수
def findLcationWithImage(fileName, startPos, confidence=.7):
    file_path = os.path.dirname(os.path.realpath(__file__)) + '\\' + 'img' + '\\' + fileName
    result = pa.locateOnScreen(file_path, confidence=confidence, region=startPos)
    print('.', end=' ')
    sys.stdout.write('. ')
    sys.stdout.flush()
    if result != None:
        print('Find Image ' +  str(result))
    return result
def findImageUntil(fileName, startPos, cnt = 60, confidence=0.8, wait=0.1):
    for i in range(cnt):
        imgpos = findLcationWithImage(fileName, startPos, confidence= confidence)
        if imgpos != None:
            break
        else:
            time.sleep(wait)
    if imgpos == None:
        return None
    else:
        return imgpos
if __name__ == "__main__":

    # - init.txt 의 width와 height 값을 읽어옴
    configFile = os.path.dirname(os.path.realpath(__file__)) + '\\' + 'init.txt'
    config = configparser.ConfigParser()
    config.read(configFile)
    width = int(config['lostark_fishing']['width'])
    height = int(config['lostark_fishing']['heght'])
    region = makeRegion(getCenterOfScreen(), width, height)
    findImageUntil("LA_exclamation_mark.png", region, cnt=60, confidence=0.8)