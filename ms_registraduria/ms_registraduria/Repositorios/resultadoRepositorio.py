from Repositorios.interfazRepositorio import InterfaceRepositorio
from ModelosRegistraduria.resultados import Resultados

class ResultadoRepositorio(InterfaceRepositorio[Resultados]):
      def getSumaVotosCandidato(self):
        pipeline2= [
    {
        '$group': {
            '_id': '$candidatomodelo', 
            'sumaVotos': {
                '$sum': '$numerovotos'
            }, 
            'numCandidato': {
                '$sum': 1
            }
        }
    }, {
        '$lookup': {
            'from': 'candidatomodelo', 
            'localField': '_id.$id', 
            'foreignField': '_id', 
            'as': 'candidato'
        }
    }, {
        '$set': {
            'candidato': {
                '$first': '$candidato'
            }
        }
    }, {
        '$addFields': {
            'idPartido1': '$candidato.idPartido.$id'
        }
    }, {
        '$lookup': {
            'from': 'partidomodelo', 
            'localField': 'idPartido1', 
            'foreignField': '_id', 
            'as': 'partido'
        }
    }, {
        '$set': {
            'partido': {
                '$first': '$partido'
            }
        }
    }, {
        '$sort': {
            'sumaVotos': -1
        }
    }, {
        '$project': {
            'CandidatoN': '$candidato.nombre', 
            'CandidatoA': '$candidato.apellido', 
            'Partido': '$partido.nombrePartido', 
            'Votos': '$sumaVotos'
        }
    }
]

        return self.queryAggregation(pipeline2)

      def getSumaVotosMesa(self):
            pipeline= [
    {
        '$group': {
            '_id': '$mesas', 
            'sumaVotos': {
                '$sum': '$numerovotos'
            }
        }
    }, {
        '$lookup': {
            'from': 'mesas', 
            'localField': '_id.$id', 
            'foreignField': '_id', 
            'as': 'mesas'
        }
    }, {
        '$set': {
            'mesas': {
                '$first': '$mesas'
            }
        }
    }, {
        '$sort': {
            'sumaVotos': -1
        }
    }, {
        '$project': {
            'Puesto': '$mesas.puesto', 
            'Ciudad': '$mesas.ciudad', 
            'Partido': '$partido.nombrePartido', 
            'Votos': '$sumaVotos'
        }
    }
]
            return self.queryAggregation(pipeline)

      def getSumaVotosPartido(self):
        pipeline2= [
    {
        '$lookup': {
            'from': 'candidatomodelo', 
            'localField': 'candidatomodelo.$id', 
            'foreignField': '_id', 
            'as': 'candidato'
        }
    }, {
        '$set': {
            'candidato': {
                '$first': '$candidato'
            }
        }
    }, {
        '$group': {
            '_id': '$candidato.idPartido.$id', 
            'sumaVotos': {
                '$sum': '$numerovotos'
            }, 
            'idPartido': {
                '$first': '$candidato.idPartido'
            }
        }
    }, {
        '$sort': {
            'sumaVotos': -1
        }
    }, {
        '$lookup': {
            'from': 'partidomodelo', 
            'localField': 'idPartido.$id', 
            'foreignField': '_id', 
            'as': 'partido1'
        }
    }, {
        '$set': {
            'partido1': {
                '$first': '$partido1'
            }
        }
    }, {
        '$project': {
            'Nombre Partido': '$partido1.nombrePartido', 
            'Lema': '$partido1.lemaPartido', 
            'Votos': '$sumaVotos'
        }
    }
]
        return self.queryAggregation(pipeline2)

      def getSumaVotosPorcentaje(self):
        pipeline2= [
    {
        '$group': {
            '_id': '$candidatomodelo', 
            'sumaVotos': {
                '$sum': '$numerovotos'
            }
        }
    }, {
        '$lookup': {
            'from': 'candidatomodelo', 
            'localField': '_id.$id', 
            'foreignField': '_id', 
            'as': 'candidato'
        }
    }, {
        '$set': {
            'candidato': {
                '$first': '$candidato'
            }
        }
    }, {
        '$lookup': {
            'from': 'partidomodelo', 
            'localField': 'candidato.idPartido.$id', 
            'foreignField': '_id', 
            'as': 'partido'
        }
    }, {
        '$set': {
            'partido': {
                '$first': '$partido'
            }
        }
    }, {
        '$sort': {
            'sumaVotos': -1
        }
    }, {
        '$limit': 15
    }, {
        '$group': {
            '_id': '$partido', 
            'votosPartido': {
                '$count': {}
            }
        }
    }, {
        '$addFields': {
            'porcentaje': {
                '$multiply': [
                    {
                        '$divide': [
                            '$votosPartido', 15
                        ]
                    }, 100
                ]
            }
        }
    }
]
        return self.queryAggregation(pipeline2)


      def getSumaVotosMesaEsp(self,idMesa):
        query1 = [
    {
        '$match': {
            'mesas.$id': ObjectId(idMesa)
        }
    }]
        query2 = [{
        '$group': {
            '_id': '$candidatomodelo', 
            'sumaVotos': {
                '$sum': '$numerovotos'
            }, 
            'numeroCandidatos': {
                '$sum': 1
            }
        }
    }, {
        '$sort': {
            'sumaVotos': -1
        }
    }
]
        pipeline = [query1, query2] 
        return self.queryAggregation(pipeline)