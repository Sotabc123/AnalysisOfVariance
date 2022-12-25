import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.formula.api import ols
import statsmodels.api as sm



data = pd.read_csv('')

data_melt = data.melt(var_name='group', value_name='A')
# data_melt['Solvent'].loc[14] = 'B'
# data_melt['Weight'].loc[14] = 72
print(data_melt)

model = ols('Weight ~ Solvent', data=data_melt).fit()                

anova = sm.stats.anova_lm(model, typ=2)
print(anova)
