import numpy as np
from sklearn.linear_model import LogisticRegression

x = np.array([[1000], [1200], [1500], [1800], [2000]])
y = np.array([0, 0, 1, 1, 1])

model = LogisticRegression()
model.fit(x, y)

new_house_size = np.array([[75]])
predicted_class = model.predict(new_house_size)
predicted_probability = model.predict_proba(new_house_size)

print("Training house sizes: ", x.flatten())
print("Purchase labels: ", y)
print("Test House: ", new_house_size[0][0])
print("Purchase prediction: ", predicted_class[0])
print("Prediction probability: ", predicted_probability)
