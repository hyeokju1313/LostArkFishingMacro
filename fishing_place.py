import os
import configparser
import mouse as mo
import keyboard as key
from ast import literal_eval

# F12를 누르면 현재 마우스의 좌표를 보여주는 함
def getMousePoint(cnt):
    state = False
    returnList = []
    tcnt = 0
    while True:
        val = key.is_pressed('F12')
        if state != val:
            if val == True:
                tcnt += 1
                returnList.append(mo.get_position())
                print ('Point ', tcnt, 'Catched')
            state = val
        if tcnt >= cnt:
            return returnList

# 낚시 장소 및 포인트 저장
def writeOptionOnConfig(section, option, val):
    flag = False
    configFile = os.path.dirname(os.path.realpath(__file__)) + '\\' + 'init.txt'
    config = configparser.ConfigParser()
    config.read(configFile)
    for idx, sec in enumerate(config.sections()):
        if sec == section:
            config[section][option] = val
            flag = True
    if flag == False:
        config.add_section(section)
        config[section][option] = val
    with open(configFile, 'w') as config_file:
        config.write(config_file)
    pass
def writeFishingPos(fishingPlace):
    poss = getMousePoint(3)
    prefixFishingPlace = 'fishingpoint_' + fishingPlace
    for i, pos in enumerate(poss):
        opt = 'point' + str(i+1)
        print(opt, ' ', pos)
        writeOptionOnConfig(prefixFishingPlace, opt, str(pos))
def saveFishingPlacePoint():
    name = input('FishingPlaceName :')
    print("move mouse cursor to water and press F12")
    writeFishingPos(name)

# 낚시 장소 및 포인트 조회
def getFishingPlaceList():
    configFile = os.path.dirname(os.path.realpath(__file__)) + '\\' + 'init.txt'
    returnList = []
    config = None
    try:
        config = configparser.ConfigParser()
        config.read(configFile)
        for section in config.sections():
            if section.find('fishingpoint') >= 0:
                returnList.append(section)
    except Exception as e:
        print(str(e))
    return returnList, config
def getFishingPointList():
    returnList, config = getFishingPlaceList()
    pointList = []
    placeList = []
    if len(returnList) > 0:
        strs = ''
        for idx, place in enumerate(returnList):
            strs += str(idx) + '. ' + place + '\n'
            placeList.append(place)
        strs += '**selectPlace : '
        index = int(input(strs))
        if index < 0 and index > len(returnList):
            print('invalid Index')
            return False
        if config != None:
            for i in config[returnList[index]]:
                pointList.append(literal_eval(config[returnList[index]][i]))
    return pointList
if __name__ == "__main__":
    opt = 0
    if opt == 0:
        saveFishingPlacePoint()
    else:
        result = getFishingPointList()
        print(result)