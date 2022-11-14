from Repositorios.interfazRepositorio import InterfaceRepositorio
from ModelosRegistraduria.candidatoModelo import CandidatoModelo
from bson import ObjectId

class CandidatoRepositorio(InterfaceRepositorio[CandidatoModelo]):
    def candidatosInscritos(self, idPartido):
      theQuery = {'idPartido.$id': ObjectId(idPartido)}
      return self.query(theQuery)