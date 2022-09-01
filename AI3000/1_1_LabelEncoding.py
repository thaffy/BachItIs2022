import pandas as pd
import numpy as numpy
from sklearn import preprocessing as preprop

input_labels = ['red','black','red','green','black','yellow','white']

encoder = preprop.LabelEncoder()
encoder.fit(input_labels)

print("\nLabel Mapping:")
for i, item in enumerate(encoder.classes_):
    print(item, '--->',i)

test_labels = ['green', 'red', 'black']
encoded_values = encoder.transform(test_labels)
print("\nLabels =",test_labels)
print("Encoded values =",encoded_values)

encoded_values = [3,0,4,1]
decoded_list = encoder.inverse_transform(encoded_values)
print("\nEncoded values=",encoded_values)
print("Decoded values =",decoded_list)

