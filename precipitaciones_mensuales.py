
from mrjob.job import MRJob
import json
from datetime import datetime

class PrecipitacionPorMes(MRJob):

    def mapper(self, _, line):
        try:
            data = json.loads(line)
            fechas = data['daily']['time']
            precipitaciones = data['daily']['precipitation_sum']

            for fecha_str, lluvia in zip(fechas, precipitaciones):
                mes = datetime.strptime(fecha_str, '%Y-%m-%d').strftime('%Y-%m')
                yield mes, lluvia
        except Exception as e:
            print(e)

    def reducer(self, mes, lluvias):
        yield mes, round(sum(lluvias), 2)

if __name__ == '__main__':
    PrecipitacionPorMes.run()