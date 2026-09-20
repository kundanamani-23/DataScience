import  matplotlib.pyplot as plt

y1=[]
y2=[]
x=range(-100,100,10)

for i in x:
  y1.append(i**2)
for i in x:
  y2.append(-i**2)
  
plt.plot(x,y1)
plt.plot(x,y2)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple graph")
plt.axhline(color = 'red')
plt.axhline(color = 'green')
plt.axvline()
plt.show()