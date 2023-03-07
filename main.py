#William Bukowski, author: Basics in ML

#this implemention will utilize scikit-learn open source library

from sklearn import datasets
from sklearn import svm

clf = svm.SVC(gamma=0.001, c=100.)