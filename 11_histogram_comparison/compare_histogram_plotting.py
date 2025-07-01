import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


age = np.random.randint(1, 100, size=100)

plt.figure()
plt.hist(age)

plt.figure()
sns.histplot(age)

plt.show()