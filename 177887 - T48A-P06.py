#Flores García Yahir Gerardo - 177887

import pandas as pd

from google.colab import drive
drive.mount('/content/drive')

#Importar datos de archivo CSV
student_df = pd.read_csv("/content/drive/MyDrive/P06 - Minería/STUDENT_GROUP.csv")
student_df.head()

attendance_df = pd.read_csv("/content/drive/MyDrive/P06 - Minería/attendance.csv")
attendance_df.head()

student_df.dtypes
attendance_df.dtypes

# Renombrar la columna STUDENT_ID para que coincida
attendance_df = attendance_df.rename(columns={'STUDENT_ID': 'student_id'})

# Convertir ambos a string
attendance_df['student_id'] = attendance_df['student_id'].astype(str)
student_df['student_id'] = student_df['student_id'].astype(str)

# Ahora si se puede hacer el merge (intersección)
merged_df = pd.merge(student_df, attendance_df, on='student_id', how='inner')

print(merged_df.head())

merged_df.dtypes

import pytz

# Convertir 'DTTM' a datetime
merged_df['DTTM'] = pd.to_datetime(merged_df['DTTM'])

# Asignar zona horaria UTC (si no tiene info de zona horaria)
merged_df['DTTM'] = merged_df['DTTM'].dt.tz_localize('UTC')

# Convertir a zona horaria local UTC-6 y sobreescribir la columna original
merged_df['DTTM'] = merged_df['DTTM'].dt.tz_convert('Etc/GMT+6')

merged_df['DT'] = merged_df['DTTM'].dt.date

# Mostrar el resultado
print(merged_df.head())

# Crear semana base (lunes como inicio de semana)
merged_df['week_start'] = pd.to_datetime(merged_df['DT']) - pd.to_timedelta(
    pd.to_datetime(merged_df['DT']).dt.weekday, unit='D'
)

# Generar combinaciones alumno–semana
all_weeks = merged_df['week_start'].drop_duplicates()
students = student_df[['student_id', 'group_id']].drop_duplicates()
all_combinations = students.assign(key=1).merge(
    pd.DataFrame({'week_start': all_weeks, 'key': 1}), on='key'
).drop('key', axis=1)

# Marcar asistencia
attendance = merged_df[['student_id', 'week_start']].drop_duplicates()
attendance['present'] = True
attendance_full = all_combinations.merge(
    attendance, on=['student_id', 'week_start'], how='left'
)
attendance_full['absent'] = attendance_full['present'].isna()

# Contar faltas por grupo y semana
faltas_por_semana = (
    attendance_full
    .groupby(['group_id', 'week_start'])
    .agg(absences=('absent', 'sum'),
         group_size=('student_id', 'count'))
    .reset_index()
)
faltas_por_semana['absence_rate'] = faltas_por_semana['absences'] / faltas_por_semana['group_size'] * 100

# Filtrar semanas con datos "reales" ---
weekly_counts = merged_df.groupby('week_start').size().reset_index(name='n_records')
good_weeks = weekly_counts.loc[weekly_counts['n_records'] >= 20, 'week_start']
faltas_filtrado = faltas_por_semana[faltas_por_semana['week_start'].isin(good_weeks)]

# Mostrar top N semanas con más faltas por grupo
TOP_N = 3
top_faltas = (
    faltas_filtrado
    .sort_values(['group_id', 'absences'], ascending=[True, False])
    .groupby('group_id', group_keys=False)
    .apply(lambda df: df.head(TOP_N), include_groups=True)
)

print("Top semanas con más faltas (filtrando semanas con >=20 registros globales):")
print(top_faltas)

# Grupo con mayor número de faltas en una semana
worst_week = faltas_filtrado.loc[faltas_filtrado['absences'].idxmax()]
print("\nMayor número de faltas en una semana (resumen):")
print(worst_week)
