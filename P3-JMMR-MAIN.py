import pandas as pd

df = pd.read_csv('Defunciones-Covid-A2.csv')

#Asignacion de los datos de las personas que han fallecido
conteo_sexo = df['sexo'].value_counts()
edad_promedio = df['edad'].mean()
edad_minima_fallecidos = int(df['edad'].min())
edad_maxima_fallecidos = int(df['edad'].max())
sumatoria_edad = df['edad'].sum()
lugar_de_fallecimiento = df['lugar_defuncion'].mode()[0]
varianza_edad = df['edad'].var()
desviacion_estandar_edad = df['edad'].std()
asimetria_edad = df['edad'].skew()
kurtosis_edad = df['edad'].kurtosis()

#Impresion de los datos
print('*Los datos de la base de datos de las Defunciones de Covid, son los siguientes.*\n\n')

print('Conteo de personas fallecidas:\n',conteo_sexo)
print('Edad Promedio de fallecidos:', edad_promedio)
print('Edad mínima de los fallecidos:', edad_minima_fallecidos)
print('Edad maxima de los fallecidos:', edad_maxima_fallecidos)
print('Sumatoria de los fallecidos:', sumatoria_edad)
print('Lugar de fallecimiento mas comun:',lugar_de_fallecimiento)
print('Varianza de los fallecidos:', varianza_edad)
print('Desviación estándar de los fallecidos:', desviacion_estandar_edad)
print('Asimetria de los fallecidos:', asimetria_edad)
print('Kurtosis de los fallecidos:', kurtosis_edad)

