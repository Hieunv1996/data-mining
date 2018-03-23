# -*- coding: utf8 -*-
"""
Load train & test data
"""
from news import News
import config

TRAIN_PATH = config.TRAIN_PATH
TEST_PATH = config.TEST_PATH


def load_train_data():
    train_data = News()
    train_data.set_target_names(config.TARGET_NAMES)
    data = []
    targets = []
    with open(TRAIN_PATH, encoding='utf-8') as f:
        list_news = f.readlines()
        for news in list_news:
            if news and len(news) > 100:
                news = news.strip()
                data.append(news[:-2])
                targets.append(int(news[-1:]))
    train_data.set_target(targets)
    train_data.set_data(data)
    return train_data


def load_test_data():
    test_data = News()
    test_data.set_target_names(config.TARGET_NAMES)
    data = []
    targets = []
    with open(TEST_PATH, encoding='utf-8') as f:
        list_news = f.readlines()
        for news in list_news:
            if news and len(news) > 100:
                news = news.strip()
                data.append(news[:-2])
                targets.append(int(news[-1:]))
    test_data.set_target(targets)
    test_data.set_data(data)
    return test_data
