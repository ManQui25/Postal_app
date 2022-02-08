from flask import Flask
from flask import jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app) ## To allow direct AJAX calls

@app.route('/', methods=['GET'])
def main():
    return jsonify({
                '/random': 'Devuelve un código postal al azar',
                '/lon&lat': 'Al ingresar la longitud y la latitud de un lugar devuelve su código postal, si no los encuentra devuelve resultado null. Ej: 0.164188 & 51.48063',
                '/postal-code/id': 'Trae tanto la longitud como la latitud de una de las coordenadas que se encontraban en el archivo cvs y se cargaron al microservicio de almacenamiento, por límites de almacenamiento el valor debe estar entre 1 a 999'
})


@app.route('/random', methods=['GET'])
def home():
    r = requests.get('http://api.postcodes.io/random/postcodes')
    return r.json()

@app.route('/<string:lon>&<string:lat>', methods=['GET'])
def test(lon, lat):
    if (lon == "null" and  lat == "null") :
        return 'Error de datos'
    else: 
        r = requests.get('https://api.postcodes.io/postcodes?lon='+lon+'&lat='+lat+'&limit=1')
        return r.json()

@app.route('/postal-code/<string:id>', methods=['GET'])
def postal(id):
    if int(id) < 0:
        return 'Ingresa una URL válida (entre 1 a 999)'
    r = requests.get('https://morning-plateau-36411.herokuapp.com/postal/'+id).text
    if len(r) > 2:
        l=eval(r)
        h = l[0]
        lon = h['lon']
        lon = str(lon)
        lat = h['lat']
        lat = str(lat)
        result = requests.get('https://api.postcodes.io/postcodes?lon='+lon+'&lat='+lat+'&limit=1')
        return result.json()
        
    else:
        return 'Ingresa una URL válida (entre 1 a 999)'

#PARA DESPLIEGUE A DOCKER O A LA NUBE
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

#PARA USO LOCAL UNICAMENTE
#if __name__ == '__main__':
#    app.run(debug=True)
