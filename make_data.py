# -*- coding: utf8 -*-
"""
Make train and test data from master data
"""
import config
import Logger
from random import shuffle

logger = Logger.Logger("make_data", config.LOG_MAKE_DATA)
from os import listdir
from os.path import isfile
import traceback

TRAIN_PATH = config.TRAIN_PATH
TEST_PATH = config.TEST_PATH
DATA_DIR = config.MASTER_DATA_DIR
NUMBER_OF_NEWS = config.NUMBER_OF_NEWS
TRAIN_PERCENT = config.TRAIN_PERCENT


def read(file_path, deval=''):
    try:
        with open(file_path, encoding='utf-8') as f:
            lines = f.readlines()
            shuffle(lines)
            return lines
    except Exception as e:
        logger.error('Error in read: ' + str(e))


def save_to_file(data, path):
    try:
        with open(path, mode='w+', encoding='utf-8') as f:
            for data_item in data:
                f.write(data_item)
        logger.info(path + '- Write success!')
    except Exception as e:
        logger.error('Error in save_to_file: ' + str(e))


def clean(data):
    clean_data = []
    for item in data:
        if item and len(item) > 100:
            clean_data.append(item)
    return clean_data

def make_data():
    train_data = []
    test_data = []
    try:
        for file in listdir(DATA_DIR):
            file = DATA_DIR + file
            list_news = read(file, '')
            if isfile(file):
                if list_news:
                    if len(list_news) > NUMBER_OF_NEWS:
                        list_news = list_news[:NUMBER_OF_NEWS]
                    last_train_index = int(len(list_news) * TRAIN_PERCENT)
                    train_data.extend(list_news[:last_train_index])
                    test_data.extend(list_news[last_train_index:])
            else:
                logger.debug('Dir: ' + file)

        train_data = clean(train_data)
        test_data = clean(test_data)

        logger.info('Train size: %d' % len(train_data))
        logger.info('Test size: %d' % len(test_data))

        save_to_file(train_data, TRAIN_PATH)
        save_to_file(test_data, TEST_PATH)
    except Exception as e:
        logger.error('Error in make_data: ' + str(e))
        traceback.print_exc()


if __name__ == '__main__':
    make_data()
