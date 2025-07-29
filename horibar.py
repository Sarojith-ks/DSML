import numpy as np
import matplotlib.pyplot as plt
x=np.array(['Java','Python','PHP','Javascript','C#','C++'])
y=np.array([22.2,17.6,8.8,8,7.7,6.7])
colors=['red', 'yellow', 'blue', 'green', 'pink', 'grey']
plt.title('bar Chart')
plt.ylabel('Programming Language')
plt.xlabel('Popularity')
plt.barh(x,y,color=colors)
plt.show()
