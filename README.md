# Análisis de Precipitación Mensual con Hadoop MapReduce y Flask API

---

## 🎯 Objetivo

Implementar una arquitectura batch distribuida basada en Hadoop utilizando Amazon EMR, procesando datos climáticos con MapReduce (MRJob en Python), y exponiendo los resultados mediante una API construida con Flask.

---

## 🗃️ Fuente de Datos

Se utilizó la API de **Open-Meteo** para obtener datos históricos de precipitación en Medellín:

- URL base: `https://archive-api.open-meteo.com/v1/archive?latitude=6.25&longitude=-75.56&start_date=2024-01-01&end_date=2024-12-31&daily=precipitation_sum&timezone=America/Bogota`
- Variables: `precipitation_sum`
- Formato: JSON

---

## Flujo del Proyecto

1. **Obtención de datos:**
   - Se descargó manualmente un archivo `datos.json` con datos climáticos.

2. **Carga en HDFS:**
   ```bash
   hdfs dfs -mkdir /user/admin/datosP3
   hdfs dfs -copyFromLocal datos.json /user/admin/datosP3/

3. **Procesamiento MapReduce (MRJob):**

    - Script: precipitacion_mensual.py

    - Agrupa las precipitaciones por mes y las suma.

    - Ejecución:

    ```bash
    python3 precipitacion_mensual.py hdfs:///user/admin/datosP3/datos.json \ 
    -r hadoop --output-dir hdfs:///user/admin/resultadosPorMes

4. **Descarga de resultados:**

    ```bash
    hdfs dfs -getmerge /user/admin/resultadosPorMes precipitacion_mensual.csv

5. **Visualización con API Flask:**

    - Script: api_flask.py

    - Endpoint: http://<IP_PUBLICA>:5000/precipitacion-mensual

---

## Automatización del flujo con Bash

    Se creó un script procesar_precipitacion.sh para ejecutar todo el flujo automáticamente

---

## API Flask

    La API sirve los datos generados por MapReduce en formato JSON.

## Ejecutar API

    ```bash
    pip3 install flask --user
    python3 api_flask.py

    La API estará disponible en:
    http://<IP_PUBLICA>:5000/precipitacion-mensual

