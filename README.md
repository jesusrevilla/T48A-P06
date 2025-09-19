# T48A-P06

Frecuentemente los datos de entrada requieren un tratamiento antes de ser utilizados.  
Los archivos attendace.csv y STUDENT_GROUP.csv son un ejemplo en el que los datos   
se analizan mejor si se realizan algunas transformaciones antes de utilizarlos.   

## En una libreta de colab

1) Importe los archivos csv y conviertalos a pandas dataframe   
2) Utilice el método describe de pandas para entender los tipos de datos   
3) Transforme uno de los dataframes para poder realizar un merge (join: intersección) entre los dataframes   
4) El timestamp esta en UTC   
5) Cambie el timestamp a su hora local   
6) Genere un reporte de los días en los que los alumnos faltan más por cada grupo   
