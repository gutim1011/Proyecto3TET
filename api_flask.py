from flask import Flask, jsonify
import csv

app = Flask(__name__)


@app.route('/precipitacion-mensual')
def mostrar_precipitacion():
    resultados = []
    with open('precipitacion_mensual.csv', newline='') as archivo:
        lector = csv.reader(archivo, delimiter='\t')
        for fila in lector:
            if len(fila) < 2:
                continue
            mes = fila[0].strip('"')
            try:
                precipitacion = float(fila[1])
            except ValueError:
                continue
            resultados.append({'mes': mes, 'precipitacion': precipitacion})

    resultados.sort(key=lambda x: x['mes'])
    return jsonify(resultados)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)