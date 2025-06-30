import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = {
	"Country": ["Hungary", "Germany", "France", "Spain"],
	"GPD": [200, 350, 400, 250]
}

df = pd.DataFrame(data)

sns.barplot(y = 'Country', x = 'GPD', data = df, palette = "Blues")


plt.savefig("10_barplot_comparsion.png")
plt.show()