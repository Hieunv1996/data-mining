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
# Online demo:
[https://data-mining-epu.herokuapp.com/](https://data-mining-epu.herokuapp.com/)
