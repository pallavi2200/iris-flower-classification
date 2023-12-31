import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.datasets import load_iris

url="https://raw.githubusercontent.com/pallavi2200/iris-flower-classification/main/iris%20dataset/IRIS%20(3).csv"
data = pd.read_csv(url)
data.head()

iris = load_iris()

data = pd.DataFrame(data=np.c_[iris['data'], iris['target']], columns=iris['feature_names'] + ['target'])

X = data[['petal length (cm)', 'sepal length (cm)']]
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

print(classification_report(y_test, y_pred))
confusion = confusion_matrix(y_test, y_pred)
print('Confusion Matrix:')
print(confusion)

def predict_species(petal_length, sepal_length):
    input_data = pd.DataFrame({'petal length (cm)': [petal_length], 'sepal length (cm)': [sepal_length]})

    species_id = model.predict(input_data)[0]

    species_names = iris['target_names'][int(species_id)]

    return species_names

# Example usage:
petal_length = 4.8
sepal_length = 3.0

predicted_species = predict_species(petal_length, sepal_length)
print(f'Predicted species 1: {predicted_species}')

# Example 2
petal_length_1 = 4.5
sepal_length_1 = 3.0
predicted_species_1 = predict_species(petal_length_1, sepal_length_1)
print(f'Predicted species 2: {predicted_species_1}')

# Example 3
petal_length_2 = 5.7
sepal_length_2 = 3.5
predicted_species_2 = predict_species(petal_length_2, sepal_length_2)
print(f'Predicted species 3: {predicted_species_2}')

# Example 4
petal_length_3 = 1.0
sepal_length_3 = 4.0
predicted_species_3 = predict_species(petal_length_3, sepal_length_3)
print(f'Predicted species 4: {predicted_species_3}')
