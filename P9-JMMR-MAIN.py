import os
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

def generar_grafica(df, nombre_archivo, num_registros):
    df['fecha_defuncion'] = pd.to_datetime(df['fecha_defuncion'])

    fecha_inicio = df['fecha_defuncion'].iloc[0]
    df['dias_tras_la_muerte'] = (df['fecha_defuncion'] - fecha_inicio).dt.days

    df_promedio = df.groupby('dias_tras_la_muerte')['edad'].mean().reset_index()

    X = sm.add_constant(df_promedio['dias_tras_la_muerte'])
    Y = df_promedio['edad']
    modelo = sm.OLS(Y, X).fit()

    confianza_intervalo = modelo.get_prediction(X).conf_int()

    dias_futuros = pd.DataFrame({'dias_tras_la_muerte': range(df_promedio['dias_tras_la_muerte'].max() + 1, df_promedio['dias_tras_la_muerte'].max() + 100)})
    X_futuro = sm.add_constant(dias_futuros['dias_tras_la_muerte'])
    prediccion_futuro = modelo.predict(X_futuro)

    plt.figure(figsize=(10, 6))
    plt.scatter(df_promedio['dias_tras_la_muerte'], df_promedio['edad'], label='Edades', alpha=0.7)
    plt.plot(df_promedio['dias_tras_la_muerte'], modelo.predict(X), color='red', label='Recta de Regresión')
    plt.plot(dias_futuros['dias_tras_la_muerte'], prediccion_futuro, linestyle='dashed', color='blue', label='Forecasting')

    plt.fill_between(df_promedio['dias_tras_la_muerte'], confianza_intervalo[:, 0], confianza_intervalo[:, 1], color='gray', alpha=0.3, label='Intervalo de Confianza')

    plt.xlabel('Días Transcurridos desde {}'.format(fecha_inicio.date()))
    plt.ylabel('Edad de los fallecidos')
    plt.title('Regresion lineal: Días transcurridos vs. promedio de edad de los fallecidos con Forecasting ({} registros)'.format(num_registros))
    plt.legend()
    plt.yticks(range(int(min(Y)), int(max(Y)) + 1))
    plt.savefig(os.path.join(nombre_archivo))
    plt.tight_layout()
    plt.show()

df_5k = pd.read_csv('Defunciones-Covid-A2.csv', nrows=5000)
generar_grafica(df_5k, 'P9-RLF1.png', 5000)

df_60k = pd.read_csv('Defunciones-Covid-A2.csv', nrows=60000)
generar_grafica(df_60k, 'P9-RLF2.png', 60000)

df_175k = pd.read_csv('Defunciones-Covid-A2.csv', nrows=175000)
generar_grafica(df_175k, 'P9-RLF3.png', 175000)


