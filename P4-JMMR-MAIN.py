import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Defunciones-Covid-A2.csv')

#Graficas de barras

conteo_sexo = df['sexo'].value_counts()
plt.bar(conteo_sexo.index, conteo_sexo.values)
plt.xlabel('Genero')
plt.ylabel('Cantidad de fallecidos')
plt.title('Genero de los fallecidos por covid')
plt.savefig('Grafica_de_genero_de_fallecidos.png')
plt.close()

conteo_nacionalidad = df['nacionalidad'].value_counts()
plt.bar(conteo_nacionalidad.index, conteo_nacionalidad.values)
plt.xlabel('Nacionalidad')
plt.ylabel('Cantidad de gente perteneciente a dicha nacionalidad')
plt.title('Nacionalidad de los fallecidos por covid')
plt.savefig('Nacionalidad_de_los_fallecidos.png')
plt.close()

conteo_am = df['atencion_medica'].value_counts()
plt.bar(conteo_am.index, conteo_am.values)
plt.xlabel('Atencion medica')
plt.ylabel('Cantidad de gente que recibio atencion medica')
plt.title('Gente fallecida que recibio atencion medica')
plt.savefig('AM_de_los_fallecidos.png')
plt.close()

#Grafica de lineas

df['fecha_defuncion'] = pd.to_datetime(df['fecha_defuncion'])
df['mes'] = df['fecha_defuncion'].dt.strftime('%Y-%m')
hombres_df = df[df['sexo'] == 'hombre']
conteo_fallecimiento_h = hombres_df['mes'].value_counts().sort_index()
mujeres_df = df[df['sexo'] == 'mujer']
conteo_fallecimiento_m = mujeres_df['mes'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
plt.scatter(conteo_fallecimiento_h.index, conteo_fallecimiento_h.values, marker='o', s=50, label='H (Hombres)')
plt.scatter(conteo_fallecimiento_m.index, conteo_fallecimiento_m.values, marker='o', s=50, label='M (Mujeres)')
plt.xlabel('Mes de Fallecidos')
plt.ylabel('Cantidad de Fallecidos')
plt.title('Cantidad de Fallecimientos por Mes (Hombres vs. Mujeres)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('Grafica_fallecimiento_por_mes.png')
plt.close()

df['fecha_defuncion'] = pd.to_datetime(df['fecha_defuncion'])
df['mes'] = df['fecha_defuncion'].dt.strftime('%Y-%m')
casado_df = df[df['estado_civil'] == 'CASADO(A)']
EC_del_fallecido_casado = casado_df['mes'].value_counts().sort_index()
viudo_df = df[df['estado_civil'] == 'VIUDO(A)']
EC_del_fallecido_viudo = viudo_df['mes'].value_counts().sort_index()
soltero_df = df[df['estado_civil'] == 'SOLTERO(A)']
EC_del_fallecido_soltero = soltero_df['mes'].value_counts().sort_index()
unionl_df = df[df['estado_civil'] == 'UNION LIBRE']
EC_del_fallecido_ul = unionl_df['mes'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
plt.scatter(EC_del_fallecido_casado.index, EC_del_fallecido_casado.values, marker='o', s=50, label='C (Casado)')
plt.scatter(EC_del_fallecido_viudo.index, EC_del_fallecido_viudo.values, marker='o', s=50, label='V (Viudo)')
plt.scatter(EC_del_fallecido_soltero.index, EC_del_fallecido_soltero.values, marker='o', s=50, label='S (Soltero)')
plt.scatter(EC_del_fallecido_ul.index, EC_del_fallecido_ul.values, marker='o', s=50, label='U (Union Libre)')
plt.xlabel('Mes de los Fallecidos')
plt.ylabel('Cantidad de Fallecidos')
plt.title('Estado Civil de los Fallecidos por Mes')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('Grafica_EC_de_los_fallecidos_por_mes.png')
plt.close()

df['fecha_defuncion'] = pd.to_datetime(df['fecha_defuncion'])
df['mes'] = df['fecha_defuncion'].dt.strftime('%Y-%m')
si_df = df[df['necropsia'] == 'SI']
conteo_si = si_df['mes'].value_counts().sort_index()
no_df = df[df['necropsia'] == 'NO']
conteo_no = no_df['mes'].value_counts().sort_index()
ne_df = df[df['necropsia'] == 'NO ESPECIFICADO']
conteo_ne = ne_df['mes'].value_counts().sort_index()
se_df = df[df['necropsia'] == 'SE IGNORA']
conteo_se = se_df['mes'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
plt.scatter(conteo_si.index, conteo_si.values, marker='o', s=50, label='SI')
plt.scatter(conteo_no.index, conteo_no.values, marker='o', s=50, label='NO')
plt.scatter(conteo_ne.index, conteo_ne.values, marker='o', s=50, label='NO ESPECIFICADO')
plt.scatter(conteo_se.index, conteo_se.values, marker='o', s=50, label='SE IGNORA')
plt.xlabel('Mes de Fallecidos')
plt.ylabel('Cantidad de Fallecidos que tuvieron Necropsia')
plt.title('Cantidad de Fallecimientos que tuvieron Necropsia por Mes')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('Grafica_pacientes_que_tuvieron_necropsia_por_mes.png')
plt.close()

#Juan Manuel Martínez Ramírez
#1897962
