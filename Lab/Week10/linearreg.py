import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([[1000], [1200], [1500], [1800], [2000]])
y = np.array([50, 55, 65, 80, 90])

model = LinearRegression()
model.fit(x, y)

new_house_size = np.array([[1700]])
predicted_price = model.predict(new_house_size)
print("Training house sizes: ", x.flatten())
print("Training house prices: ", y)
print("Predicted price for a house of size 1700 sq ft: ", predicted_price[0])
