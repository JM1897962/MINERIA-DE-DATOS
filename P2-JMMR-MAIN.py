import pandas as pd 

archivo_csv = "Defunciones-Covid.csv"
df = pd.read_csv(archivo_csv)

columnas_a_eliminar = ['lengua_indigena', 'sitio_lesion', 'durante_embarazo', 'causado_embarazo', 'complicacion_embarazo', 'tipo_evento', 'en_trabajo', 'municipio_ocurrencia']
df = df.drop(columns = columnas_a_eliminar)

nuevo_archivo_csv = "Defunciones-Covid-A2.csv"
df.to_csv(nuevo_archivo_csv, index=False)

#Juan Manuel Martínez Ramírez
#1897962
