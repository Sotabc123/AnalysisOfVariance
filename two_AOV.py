import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm


data = pd.read_csv('')

formula = 'Time ~ (group) + (measure_2) + (group):(measure_2)'
model = ols(formula, data).fit()
aov_table = anova_lm(model, typ=2)
aov_table.columns = ["平方和","自由度","F値","p値"] #列名を日本語に差し替え
print(aov_table)
