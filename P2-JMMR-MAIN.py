import pandas as pd 

# Lee el archivo de la base de datos
archivo_csv = "Defunciones-Covid.csv"
df = pd.read_csv(archivo_csv)

# Elimina todas las columnas que no se deseen conservar
columnas_a_eliminar = ['lengua_indigena', 'sitio_lesion', 'durante_embarazo', 'causado_embarazo', 'complicacion_embarazo', 'tipo_evento', 'en_trabajo', 'municipio_ocurrencia']
df = df.drop(columns = columnas_a_eliminar)

# Guarda la base de datos modificada, en una nueva
nuevo_archivo_csv = "Defunciones-Covid-A2.csv"
df.to_csv(nuevo_archivo_csv, index=False)
