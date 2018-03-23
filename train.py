"""
Train and save model

"""
import pickle
import traceback

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

import Logger
import config
import load_data

logger = Logger.Logger("train", config.LOG_TRAIN)


def save_model(model, path):
    try:
        with open(path, 'wb') as fid:
            pickle.dump(model, fid)
        logger.info(path + ' - Save success!')
    except Exception as e:
        logger.error('Error in save model: ' + str(e))
        traceback.print_exc()


def nb():
    train_data = load_data.load_train_data()
    text_clf = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', MultinomialNB())])
    text_clf = text_clf.fit(train_data.get_data(), train_data.get_target())
    save_model(text_clf, config.SAVE_NB_PATH)

    # test_data = load_data.load_test_data()
    # predicted = text_clf.predict(test_data.get_data())
    # print("Naive Bayes: %f" % np.mean(predicted == test_data.get_target()))


def svm():
    train_data = load_data.load_train_data()
    text_clf_svm = Pipeline(
        [('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf-svm', SGDClassifier(loss='hinge',
                                                                                               penalty='l2', alpha=1e-3,
                                                                                               n_iter=5,
                                                                                               random_state=42))])
    text_clf_svm.fit(train_data.get_data(), train_data.get_target())
    save_model(text_clf_svm, config.SAVE_SVM_PATH)

    # test_data = load_data.load_test_data()
    # predicted_svm = text_clf_svm.predict(test_data.get_data())
    # print("SVM: %f" % np.mean(predicted_svm == test_data.get_target()))


if __name__ == '__main__':
    nb()
    svm()
