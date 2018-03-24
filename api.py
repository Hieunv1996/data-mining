# -*- coding: utf8 -*-
import load_data
from guess import TextClassification
import config
import json
from pyvi.pyvi import ViTokenizer
import traceback
from flask import Flask, request, render_template, jsonify
import sys
import os.path

cwd = os.path.dirname(os.path.realpath(__file__)) + '/'

svm_model = TextClassification(cwd + config.SAVE_SVM_PATH)
nb_model = TextClassification(cwd + config.SAVE_NB_PATH)
LABELS = config.TARGET_NAMES
app = Flask(__name__)

test_data = load_data.load_test_data()
test_contents = test_data.get_data()
test_targets = test_data.get_target()
target_name = test_data.get_target_names()


@app.route('/svm/', methods=['GET', 'POST'])
def svm():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        try:
            document = request.form['document']
            document = ViTokenizer.tokenize(document)
            if document.strip() == '':
                return render_template('index.html', message='Please enter your document.')
            print(document)
            message = LABELS[nb_model.detect_one(document)]
            print(message)
            return render_template('index.html', message=message, document=document)
        except Exception as e:
            traceback.print_exc()
            return render_template('index.html', message='Check error. See log file for detail.', document=document)


@app.route('/nb/', methods=['GET', 'POST'])
def nb():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        try:
            document = request.form['document']
            document = ViTokenizer.tokenize(document)
            if document.strip() == '':
                return render_template('index.html', message='Please enter your document.')
            print(document)
            message = LABELS[nb_model.detect_one(document)]
            print(message)
            return render_template('index.html', message=message, document=document)
        except Exception as e:
            traceback.print_exc()
            return render_template('index.html', message='Check error. See log file for detail.', document=document)


@app.route('/svm/<id>', methods=['GET'])
def svm_by_id(id):
    try:
        id = int(id)
        document = test_contents[id]
        if document.strip() == '':
            return render_template('index.html', message='Please enter your document.')
        print(document)
        message = LABELS[nb_model.detect_one(document)]
        print(message)
        return render_template('index.html', message=message, document=document, real_result=LABELS[test_targets[id]])
    except Exception as e:
        traceback.print_exc()
        return render_template('index.html', message='Check error. See log file for detail.', document=document)


@app.route('/nb/<id>', methods=['GET'])
def nb_by_id(id):
    try:
        id = int(id)
        document = test_contents[id]
        if document.strip() == '':
            return render_template('index.html', message='Please enter your document.')
        print(document)
        message = LABELS[nb_model.detect_one(document)]
        print(message)
        return render_template('index.html', message=message, document=document, real_result=LABELS[test_targets[id]])
    except Exception as e:
        traceback.print_exc()
        return render_template('index.html', message='Check error. See log file for detail.', document=document)


@app.route('/')
def guide():
    g = {'/': 'show guide', '/nb/': 'detect label using naive bayes', '/svm/': 'detect label ussing svm',
         '/key': 'show 100 item in test data from givent key(int)', '/nb/id': 'detect labe using nb from testdata[id]',
         '/svm/id': 'detect labe using nb from testdata[id]', '/checksvm': 'check svm correct',
         '/checknb': 'check nb correct'}
    return jsonify(g)


@app.route('/<key>', methods=['GET'])
def get_data_test(key):
    try:
        document = {}
        key = int(key)
        max_key = key + 100
        for content, target in zip(test_contents[key:], test_targets[key:]):
            document[key] = {'id': key, 'content': content, 'target': LABELS[target]}
            key += 1
            if key > max_key: break
        document['target_name'] = target_name
        return json.dumps(document, ensure_ascii=False)
    except:
        traceback.print_exc()
        return 'Error'


@app.route('/checksvm', methods=['GET'])
def check_svm():
    try:
        return jsonify(svm_model.predict(test_data))
    except:
        traceback.print_exc()
        return 'Error'


@app.route('/checknb', methods=['GET'])
def check_nb():
    try:
        return jsonify(nb_model.predict(test_data))
    except:
        traceback.print_exc()
        return 'Error'


if __name__ == '__main__':
    app.run('localhost', 9000)
