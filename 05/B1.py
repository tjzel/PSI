import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
import statsmodels.formula.api as smf

df_adv = pd.read_csv(
    "https://raw.githubusercontent.com/przem85/bootcamp/master/statistics/Advertising.csv",
    index_col=0,
)
df_adv.head()

est = smf.ols(
    formula="sales ~ np.sqrt(TV) + I(TV) + I(TV):I(radio) + np.sqrt(newspaper)",
    data=df_adv,
).fit()
print((est.summary2()))

sns.pairplot(df_adv)
plt.show()
