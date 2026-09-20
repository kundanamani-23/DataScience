import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("temporal.csv")
plt.plot(df['deep learning'], df['machine learning'], color='red')
plt.xlabel('deep learning')
plt.ylabel('machine learning')
plt.title('line plot')
plt.xlim(10, 100)
plt.ylim(0, 50)
plt.grid(True)
plt.show()