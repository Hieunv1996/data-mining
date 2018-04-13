# Online demo:
[https://data-mining-epu.herokuapp.com/](https://data-mining-epu.herokuapp.com/)
# Correct:
```
Naive bayes: 
{
  "correct": 0.9264248704663213, 
  "len": 1930
}
SMV:
{
  "correct": 0.9595854922279793, 
  "len": 1930
}
correct: number of correct testcase / number of testcase
len: Number of testcase
```
# Train and test data:
Data from some VietNam news website. Data use for this project is in **res** dir
```
/res/

    /---- train : train data

    /---- test: test data

    /---- master_data: Data before preprocess
```

# Requires:
- python 3.x
- Numpy
- scipy
- sklearn

# How to run
```
git clone https://github.com/Hieunv1996/data-mining && cd data-mining
pip install -U scikit-learn
pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
python api.py
```
Then you can go to [localhost:9000](localhost:9000) to see what's going on

# Document
```
{
  "/": "show guide", 
  "/checknb": "check nb correct", 
  "/checksvm": "check svm correct", 
  "/key": "show 100 item in test data from givent key(int)", 
  "/nb/": "detect label using naive bayes", 
  "/nb/id": "detect labe using nb from testdata[id]", 
  "/svm/": "detect label ussing svm", 
  "/svm/id": "detect labe using nb from testdata[id]"
}
```
