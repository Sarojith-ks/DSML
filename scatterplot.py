import numpy as np
import matplotlib.pyplot as plt
mathematics_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
plt.scatter(mathematics_marks, science_marks, color='blue', marker='o')
plt.xlabel('Math Marks')
plt.ylabel('Science Marks')
plt.title('Scatter Plot of Mathematics vs Science Marks')
plt.show()


