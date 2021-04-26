import fishing_image as fi
import fishing_place as fp
import pyautogui as pa
import random
import time
from init_config import *


# - 이미지 이름을 입력 받아 이미지가 존재하게 될경우 입력 받은 Key 이벤트 발생 -
def findImgAndPressKey(imgName, key, startPos, cnt=60, confidence=.8, wait=0.1):
    posBtn = fi.findImageUntil(imgName, startPos=startPos, cnt=cnt, confidence=confidence, wait=wait)
    if posBtn == None:
        return False

    else:
        pa.press(key)
        return True


# - 자동 낚시 main 함수 -
def fishingLostArk(wait, setPos=1, fishingKey='w'):
    fishingFailCnt = 0
    posList = []

    # - 마우스를 움직여 3개의 포인트를 지정
    if setPos == 0:
        posList = fp.getMousePointWithKey(3)
    # - init.txt 의 낚시터별 포인트를 불러옴
    else:
        posList = fp.getFishingPointList()
        print('point of init : ', str(posList))

    # - init_config.py 에서 저장한 값
    width = FISHING_WIDTH
    height = FISHING_HEIGHT

    # - 자동 낚시 무한 반복 -
    while True:
        # - 20번이상 실패하면 프로그램 종료 -
        if fishingFailCnt > 20:
            print("Fishing Too Much Fail")
            return

        if len(posList) > 0:
            idx = random.randrange(0, len(posList))
            #  idx = fising_cnt % 3
            pa.moveTo(posList[idx][0], posList[idx][1], 1)
        else:
            print("Can't get fishing point")
            return

        pa.press(fishingKey)
        time.sleep(1)

        # - 느낌표를 검출할 영역
        region = fi.makeRegion(fi.getCenterOfScreen(), width, height)

        res = findImgAndPressKey(FISHING_EXCLAMATION_MARK_IMG_NAME, fishingKey, startPos=region,
                                 cnt=FISHING_EXCLAMATION_MARK_DETECT_CNT, confidence=0.8, wait=0.1)
        if res == True:
            print('Fishing Success')
            time.sleep(wait)
            if fishingFailCnt > 0:
                fishingFailCnt -= 1
        else:
            print('fishing Fail')
            fishingFailCnt += 1
            time.sleep(2)


if __name__ == "__main__":
    fishingLostArk(FISHING_WAIT_TIME, setPos=1, fishingKey='w')