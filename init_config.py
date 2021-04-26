import configparser
import os
configFile = os.path.dirname(os.path.realpath(__file__)) + '\\' + 'init.txt'
config = configparser.ConfigParser()
config.read(configFile)
FISHING_WIDTH = int(config['lostark_fishing']['width'])
FISHING_HEIGHT = int(config['lostark_fishing']['height'])
FISHING_WAIT_TIME = int(config['lostark_fishing']['wait_time'])
FISHING_EXCLAMATION_MARK_IMG_NAME = config['lostark_fishing']['mark_image_name']
FISHING_EXCLAMATION_MARK_DETECT_CNT = int(config['lostark_fishing']['detect_cnt'])