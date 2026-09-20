import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("temporal.csv")
plt.plot(df['Mes'], df['data science'], label = 'data science')
plt.plot(df['Mes'], df['machine learning'], label = 'machine learning')
plt.plot(df['Mes'], df['deep learning'], label = 'deep learning')
plt.xlabel('Date')
plt.ylabel('Popularity')
plt.title('Popularity of AI terms by date')
plt.grid(True)
plt.legend()
plt.show()