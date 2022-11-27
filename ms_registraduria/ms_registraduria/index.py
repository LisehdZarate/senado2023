from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from ControladoresRegistraduria.candidatoControlador import CandidatoControlador
from ControladoresRegistraduria.mesaControlador import MesaContralador
from ControladoresRegistraduria.mesaVotanteControlador import MesaVotanteControlador
from ControladoresRegistraduria.partidoControlador import PartidoControlador
from ControladoresRegistraduria.resultadoControlador import ResultadoControlador


app=Flask(__name__)
cors = CORS(app)

_controlador_candidato=CandidatoControlador()
_controlador_mesa=MesaContralador()
_controlador_mesaVotante=MesaVotanteControlador()
_controlador_partido=PartidoControlador()
_controlador_resultado=ResultadoControlador()

@app.route('/server',methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)

#################################################CANDIDATO################################################3##############################

@app.route('/candidatos',methods=['GET'])
def listarCandidato():
    datos_salida=_controlador_candidato.listarCandidato()
    return jsonify(datos_salida)

@app.route('/candidatos',methods=['POST'])
def crearCandidato():
    datos_entrada = request.get_json()
    datos_salida=_controlador_candidato.crearCandidato(datos_entrada)
    return jsonify(datos_salida)

@app.route('/candidatos/<string:id>',methods=['GET'])
def mostrarCandidato(id):
    datos_salida=_controlador_candidato.mostrarCandidato(id)
    return jsonify(datos_salida)

@app.route('/candidatos/<string:id>',methods=['PUT'])
def modificarCandidato(id):
    datos_entrada = request.get_json()
    datos_salida=_controlador_candidato.actualizarCandidato(id,datos_entrada)
    return jsonify(datos_salida)

@app.route('/candidatos/<string:id>',methods=['DELETE'])
def eliminarCandidato(id):
    datos_salida=_controlador_candidato.eliminarCandidato(id)
    return jsonify(datos_salida)


##################################################################MESAS##################################################################

@app.route('/mesas',methods=['GET'])
def listarMesa():
    datos_salida=_controlador_mesa.listarMesa()
    return jsonify(datos_salida)

@app.route('/mesas',methods=['POST'])
def crearMesa():
    datos_entrada = request.get_json()
    datos_salida=_controlador_mesa.crearMesa(datos_entrada)
    return jsonify(datos_salida)

@app.route('/mesas/<string:id>',methods=['GET'])
def mostrarMesa(id):
    datos_salida=_controlador_mesa.mostrarMesa(id)
    return jsonify(datos_salida)

@app.route('/mesas/<string:id>',methods=['PUT'])
def modificarMesa(id):
    datos_entrada = request.get_json()
    datos_salida=_controlador_mesa.actualizarMesa(id,datos_entrada)
    return jsonify(datos_salida)

@app.route('/mesas/<string:id>',methods=['DELETE'])
def eliminarMesa(id):
    datos_salida=_controlador_mesa.eliminarMesa(id)
    return jsonify(datos_salida)

###################################################3###MESASVOTANTES##############################################################

@app.route('/mesasvotantes',methods=['GET'])
def listarMesaVotante():
    datos_salida=_controlador_mesaVotante.listarMesaVotante()
    return jsonify(datos_salida)

@app.route('/mesasvotantes',methods=['POST'])
def crearMesaVotante():
    datos_entrada = request.get_json()
    datos_salida=_controlador_mesaVotante.crearMesaVotante(datos_entrada)
    return jsonify(datos_salida)

@app.route('/mesasvotantes/<string:id>',methods=['GET'])
def mostrarMesaVotante(id):
    datos_salida=_controlador_mesaVotante.mostrarMesaVotante(id)
    return jsonify(datos_salida)

@app.route('/mesasvotantes/<string:id>',methods=['PUT'])
def modificarMesaVotante(id):
    datos_entrada = request.get_json()
    datos_salida=_controlador_mesaVotante.actualizarMesaVotante(id,datos_entrada)
    return jsonify(datos_salida)

@app.route('/mesasvotantes/<string:id>',methods=['DELETE'])
def eliminarMesaVotante(id):
    datos_salida=_controlador_mesaVotante.eliminarMesaVotante(id)
    return jsonify(datos_salida)

#######################################################PARTIDOS######################################################################

@app.route('/partidos',methods=['GET'])
def listarPartido():
    datos_salida=_controlador_partido.listarPartido()
    return jsonify(datos_salida)

@app.route('/partidos',methods=['POST'])
def crearPartido():
    datos_entrada = request.get_json()
    datos_salida=_controlador_partido.crearPartido(datos_entrada)
    return jsonify(datos_salida)

@app.route('/partidos/<string:id>',methods=['GET'])
def mostrarPartido(id):
    datos_salida=_controlador_partido.mostrarPartido(id)
    return jsonify(datos_salida)

@app.route('/partidos/<string:id>',methods=['PUT'])
def modificarPartido(id):
    datos_entrada = request.get_json()
    datos_salida=_controlador_partido.actualizarPartido(id,datos_entrada)
    return jsonify(datos_salida)

@app.route('/partidos/<string:id>',methods=['DELETE'])
def eliminarPartido(id):
    datos_salida=_controlador_partido.eliminarPartido(id)
    return jsonify(datos_salida)

############################################################RESULTADOS###########################################################

@app.route('/resultados',methods=['GET'])
def listarResultado():
    datos_salida=_controlador_resultado.listarResultado()
    return jsonify(datos_salida)

@app.route('/resultados',methods=['POST'])
def crearResultado():
    datos_entrada = request.get_json()
    datos_salida=_controlador_resultado.crearResultado(datos_entrada)
    return jsonify(datos_salida)

@app.route('/resultados/<string:id>',methods=['GET'])
def mostrarResultado(id):
    datos_salida=_controlador_resultado.mostrarResultado(id)
    return jsonify(datos_salida)

@app.route('/resultados/<string:id>',methods=['PUT'])
def modificarResultado(id):
    datos_entrada = request.get_json()
    datos_salida=_controlador_resultado.actualizarResultado(id,datos_entrada)
    return jsonify(datos_salida)

@app.route('/resultados/<string:id>',methods=['DELETE'])
def eliminarResultado(id):
    datos_salida=_controlador_resultado.eliminarResultado(id)
    return jsonify(datos_salida)

@app.route("/resultado/<string:id>/mesa/<string:idMesa>",methods=['PUT'])
def asignarMesaAResultado(id,idMesa):
    json=_controlador_resultado.asignarMesa(id,idMesa)
    return jsonify(json)

@app.route("/resultado/<string:id>/candidato/<string:idCandidato>",methods=['PUT'])
def asignarCandidatoAResultado(id,idCandidato):
    json=_controlador_resultado.asignarCandidato(id,idCandidato)
    return jsonify(json)

@app.route("/resultado/votoscandidatos",methods=['GET'])
def getSumaV():
    json=_controlador_resultado.SumaVotosCandidato()
    return jsonify(json)

@app.route("/resultado/votosmesa",methods=['GET'])
def getSumaMesa():
    json=_controlador_resultado.SumaVotosMesa()
    return jsonify(json)

@app.route("/resultado/partido",methods=['GET'])
def getSumaPartido():
    json=_controlador_resultado.SumaVotosPartido()
    return jsonify(json)

@app.route("/resultado/distribucion",methods=['GET'])
def getSumaPorcentaje():
    json=_controlador_resultado.SumaVotosPorcentaje()
    return jsonify(json)

@app.route("/resultado/MesaEsp/<string:idMesa>",methods=['GET'])
def getSumaMesaEsp():
    json=_controlador_resultado.SumaVotosMesaEsp(idMesa)
    return jsonify(json)

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

####################################RELACIONES #################################

@app.route("/candidatos/<string:idCandidato>/partidos/<string:idPartido>",methods=['PUT'])
def asignarPartidoCandidato(idCandidato,idPartido):
    datos_salida=_controlador_partido.asignarPartidoCandidato(idCandidato,idPartido)
    return jsonify(datos_salida)

@app.route("/mesasvotantes/<string:idMesaVotante>/resultados/<string:idResultado>",methods=['PUT'])
def asignarMesaResultado(idMesaVotante,idResultado):
    datos_salida=_controlador_resultado.asignarMesaResultado(idMesaVotante,idResultado)
    return jsonify(datos_salida)

@app.route("/candidatos/<string:idCandidato>/resultados/<string:idResultado>",methods=['PUT'])
def asignarCandidatoResultado(idCandidato,idResultado):
    datos_salida=_controlador_resultado.asignarCandidatoResultado(idCandidato,idResultado)
    return jsonify(datos_salida)


#@app.route("/candidatos/<string:id>/partidos/<string:id_departamento>",methods=['PUT'])
#def asignarDepartamentoAMateria(id,idPartido):
 #   json=miControladorCanPar.asignarPartidoCandidato(id,idPartido)
  #  return jsonify(json)

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Servidor ejecutandose : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])