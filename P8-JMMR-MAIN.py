import pandas as pd
import matplotlib.pyplot as plt
from typing import Tuple, List
import numpy as np

def k_means(points: List[np.array], k: int, name: str) :
    dim = len(points[0])
    N = len(points)
    num_cluster = k
    iterations = 15

    x = np.array(points)
    y = np.random.randint(0, num_cluster, N)

    mean = np.zeros((num_cluster, dim))
    for t in range(iterations):
        for k in range(num_cluster):
            mean[k] = np.mean(x[y == k], axis=0)
        for i in range(N):
            dist = np.sum((mean - x[i]) ** 2, axis=1)
            pred = np.argmin(dist)
            y[i] = pred

    for kl in range(num_cluster):
        xp = x[y == kl, 0]
        yp = x[y == kl, 1]
        plt.scatter(xp, yp)
    plt.savefig(f"{name}.png")
    plt.close()
    return mean

df = pd.read_csv('Defunciones-Covid.csv')

df['hora_defuncion'] = df['hora_defuncion'].str[:2]
eliminar = ["sexo","fecha_nacimiento","nacionalidad","lengua_indigena","estado_civil","entidad_residencia","municipio_residencia","escolaridad","ocupacion","afiliacion_medica","fecha_defuncion","lugar_defuncion","entidad_defuncion","alcaldia","atencion_medica","necropsia","causa_defuncion","durante_embarazo","causado_embarazo","complicacion_embarazo","muerte_accidental_violenta","tipo_evento","en_trabajo","sitio_lesion","municipio_ocurrencia","fecha_def"]

df['hora'] = pd.to_numeric(df['hora_defuncion']) + 1

df['edad'] = df['edad']

df.loc[df['edad'] == 0, ['edad']] = 1

eliminar.append('hora_defuncion')

df = df.dropna()

df_mean = df.drop(eliminar, axis=1)
print(df_mean)
list_t = [
    (np.array(tuples[0:2]), tuples[1])
    for tuples in df_mean.itertuples(index=False, name=None)
]
points = [point for point, _ in list_t]
# LLamada a la función para obtener las agrupaciones por centros de masa del df_mean
kn = k_means(
    points,
    4,
    'kmeansEdad'
)
print(kn)


