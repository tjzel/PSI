from sklearn.datasets import load_iris
import seaborn as sns
from matplotlib import pyplot as plt
from pandas import DataFrame

iris = load_iris()
data = DataFrame(iris.data)

sns.pairplot(data)  # , kind="reg"
# sns.heatmap(data.corr(), annot=True, cmap="coolwarm", center=0)  # , kind="reg"
plt.show()
