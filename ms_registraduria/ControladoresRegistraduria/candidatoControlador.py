from Repositorios.candidatoRepositorio import CandidatoRepositorio
from Repositorios.partidoRepositorio import PartidoRepositorio
from ModelosRegistraduria.candidatoModelo import CandidatoModelo
from ModelosRegistraduria.partidoModelo import PartidoModelo

class CandidatoControlador():
     
     def __init__(self):
         self.candidatoRepositorio = CandidatoRepositorio()
         self.partidoRepositorio= PartidoRepositorio()
        
     
     def listarCandidato(self):
        datos_candidato=self.candidatoRepositorio.findAll()
        return datos_candidato
        

     def crearCandidato(self,elCandidato):
      nuevoCandidato=CandidatoModelo(elCandidato)
      return self.candidatoRepositorio.save(nuevoCandidato)
        

     def mostrarCandidato(self,id):
      elCandidato=CandidatoModelo(self.candidatoRepositorio.findById(id))
      return elCandidato.__dict__

     def actualizarCandidato(self,id,elCandidato):
      candidatoActual=CandidatoModelo(self.candidatoRepositorio.findById(id))
      candidatoActual.idCandidato=elCandidato["idCandidato"]
      candidatoActual.cedula=elCandidato["cedula"]
      candidatoActual.nombre = elCandidato["nombre"]
      candidatoActual.apellido = elCandidato["apellido"]
      candidatoActual.correo = elCandidato["correo"]
      return self.candidatoRepositorio.save(candidatoActual)
     
     def eliminarCandidato(self,id):
        return self.candidatoRepositorio.delete(id)

     def asignarPartidoCandidato(self,id,idPartido):
      partidoActual=PartidoModelo(self.partidoRepositorio.findById(id))
      candidatoActual = CandidatoModelo(self.candidatoRepositorio.findById(idPartido))
      candidatoActual.PartidoModelo=partidoActual
      return self.candidatoRepositorio.save(candidatoActual)