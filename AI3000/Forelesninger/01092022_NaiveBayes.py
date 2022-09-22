import numpy as np
import pandas as pd
import matplotlib as plt
from utilities import visualize_classifier              
from sklearn import cross_decomposition
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier


# Load files
# input_file = 'data_multivar_nb.txt' 
input_file = 'AI3000\Forelesninger\data_multivar_nb.txt'  ## <-- Relative path
data = np.loadtxt(input_file, delimiter= ',')

x,y = data[:,:-1], data[:,-1]

# Creative Naive Bayes classifier
classifier = GaussianNB()
# Input the classifier
classifier.fit(x,y)

# Predict the values for training data
y_pred = classifier.predict(x)

# Compute accuracy
accuracy = 100.0 * (y == y_pred).sum() / x.shape[0]
print("Accuracy of Naive Bayes classifier=",round(accuracy,2),"%")

# Visualize the performance of the classifier
visualize_classifier(classifier,x,y)