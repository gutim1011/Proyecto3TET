#!/bin/bash

# Rutas
INPUT_LOCAL="datos.json"
INPUT_HDFS="/user/admin/datosP3/datos.json"
OUTPUT_HDFS="/user/admin/resultadosPorMes"
RESULT_LOCAL="precipitacion_mensual.csv"

echo "Subiendo datos.json actualizado al HDFS..."
hdfs dfs -rm $INPUT_HDFS
hdfs dfs -copyFromLocal $INPUT_LOCAL $INPUT_HDFS

echo "Eliminando resultados anteriores en HDFS..."
hdfs dfs -rm -r $OUTPUT_HDFS

echo "Ejecutando MRJob..."
python3 contar_ciudades.py hdfs://$INPUT_HDFS -r hadoop --output-dir hdfs://$OUTPUT_HDFS

echo "escargando y uniendo resultados a CSV..."
hdfs dfs -getmerge $OUTPUT_HDFS datos_sin_header.csv

echo "Agregando encabezado al archivo final..."
echo "mes,precipitacion" > header.csv
cat header.csv datos_sin_header.csv > $RESULT_LOCAL
rm header.csv datos_sin_header.csv

echo "Todo listo. Archivo generado: $RESULT_LOCAL"