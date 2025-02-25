#AUTOR: Christian Aarón Zavala Sánchez 171817

#Imports
import pandas as pd
import numpy as np
import datetime

#Read Data from CSV
student_group = pd.read_csv('/content/csv/STUDENT_GROUP.csv')
attendance = pd.read_csv('/content/csv/attendance.csv')

#Limpieza de datos

#Drop Nan Values
student_group.dropna(inplace=True)
attendance.dropna(inplace=True)


#Remane columns
attendance.rename(columns={'STUDENT_ID': 'student_id'}, inplace=True) #Inplace para que sea permanente

#Drop no numeric values

attendance['student_id'] = pd.to_numeric(attendance['student_id'], errors='coerce')
attendance = attendance.dropna(subset=['student_id'])  # Elimina filas con NaN
attendance['student_id'] = attendance['student_id'].astype(np.int64)

#Merge Inner
merge = attendance.merge(student_group, on='student_id', how='inner')

data = merge[merge['DT'] >= '2025-01-01']
# data['DT'] = pd.to_datetime(data['DT'])

data = data.loc[data['group_id'] == '20251ST48A']

#Alumnos totales en clase
alumnos = data['student_id'].unique()

#Tratamiento de fechas
data['DT'] = pd.to_datetime(data['DT'])
data['DT'] = data['DT'].dt.tz_localize('America/Mexico_City', ambiguous='NaT')
data['DT'] = data['DT'] - pd.Timedelta(days=1)


asistencia_dia = data.groupby('DT')['student_id'].count().reset_index(name='Asistencia')
asistencia_dia['day_name'] = asistencia_dia['DT'].dt.day_name()

asistencia_dia['alumnos_totales'] = len(alumnos)

dias_mapping = {
    'Monday': 1,
    'Tuesday': 2,
    'Wednesday': 3,
    'Thursday': 4,
    'Friday': 5,
    'Saturday': 6,
    'Sunday': 7
}

asistencia_dia['day_number'] = asistencia_dia['day_name'].map(dias_mapping)
correlacion = asistencia_dia['Asistencia'].corr(asistencia_dia['day_number'])

correlacion

asistencia_dia
