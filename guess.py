"""
Get result and test result with model save before
"""
import config
import numpy as np
import pickle
import traceback
LABELS = config.TARGET_NAMES
from pyvi.pyvi import ViTokenizer


def load_model(path):
    try:
        with open(path, 'rb') as fid:
            model = pickle.load(fid)
            return model
    except Exception as e:
        traceback.print_exc()
        exit(0)


class TextClassification(object):
    def __init__(self, model_path):
        self.__model = load_model(model_path)

    def detect_more(self, test_data):
        """ Get label for list element """
        try:
            predicted = self.__model.predict(list(test_data))
            return predicted
        except:
            return None

    def detect_one(self, test_data):
        """ Get label for only one element """
        try:
            test_data = ViTokenizer.tokenize(test_data)
            predicted = self.__model.predict([test_data])
            return predicted[0]
        except:
            return None

    def predict(self, test_data):
        try:
            report = {'len': len(test_data.get_data())}
            predicted = self.__model.predict(test_data.get_data())
            report['correct'] = np.mean(predicted == test_data.get_target())
            return report
        except:
            pass
            return ''


if __name__ == '__main__':
    obj = TextClassification(config.SAVE_NB_PATH)
    txt = ["Tôi đi đá bóng", "Tôi là một học sinh lớp 5"]
    for i, j in zip(txt, obj.detect_more(txt)):
        print(i, ': ' + LABELS[j])
