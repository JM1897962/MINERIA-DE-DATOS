import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

df = pd.read_csv('Defunciones-Covid-A2.csv', nrows=185000)
df['fecha_defuncion'] = pd.to_datetime(df['fecha_defuncion'])
fecha_final =  df['fecha_defuncion'].iloc[0]
df['dias_tras_la_muerte'] = (df['fecha_defuncion'] - fecha_final).dt.days
df_promedio = df.groupby('dias_tras_la_muerte')['edad'].mean().reset_index()

X = sm.add_constant(df_promedio['dias_tras_la_muerte'])
Y = df_promedio['edad']

modelo = sm.OLS(Y, X).fit()

print(modelo.summary())
plt.figure(figsize=(10, 6))
plt.scatter(df_promedio['dias_tras_la_muerte'], df_promedio['edad'], label='Promedios')
plt.plot(df_promedio['dias_tras_la_muerte'], modelo.predict(X), color='red', label='Recta')
plt.xlabel('Días Transcurridos desde {}'.format(fecha_final.date()))
plt.ylabel('Promedio de la Edad de los Fallecidos')
plt.title('Regresion lineal: DTLM vs. EDLF')
plt.legend()

plt.yticks(range(int(min(Y)), int(max(Y))+1))
plt.savefig('Regresion lineal de los Fallecidos.png')
plt.tight_layout()
plt.show()

#Juan Manuel Martínez Ramírez
#1897962
