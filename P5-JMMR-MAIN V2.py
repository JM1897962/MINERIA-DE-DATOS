import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

df = pd.read_csv('Defunciones-Covid-A2.csv', nrows=22000)

modelo = ols('edad ~ fecha_defuncion', data=df).fit()
tabla_de_anova = sm.stats.anova_lm(modelo, typ=2)

print("Tabla de ANOVA:")
print(tabla_de_anova)

#Juan Manuel Martínez Ramírez
#1897962
