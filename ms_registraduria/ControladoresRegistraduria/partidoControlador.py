from Repositorios.partidoRepositorio import PartidoRepositorio
from Repositorios.candidatoRepositorio import CandidatoRepositorio
from ModelosRegistraduria.candidatoModelo import CandidatoModelo
from ModelosRegistraduria.PartidoModelo import PartidoModelo


class PartidoControlador():
    
     def __init__(self):
        self.partidoRepositorio = PartidoRepositorio()
        self.candidatoRepositorio = CandidatoRepositorio()
     
     def listarPartido(self):
        return self.partidoRepositorio.findAll()

     def crearPartido(self,elPartido):
        nuevaMesaVotante=PartidoModelo(elPartido)
        return self.partidoRepositorio.save(nuevaMesaVotante)

     def mostrarPartido(self,id):
      elpartido=PartidoModelo(self.partidoRepositorio.findById(id))
      return elpartido.__dict__

     def actualizarPartido(self,id,elPartido):
      partidoActual=PartidoModelo(self.partidoRepositorio.findById(id))
      partidoActual.idPartido=elPartido["idPartido"]
      partidoActual.nombrePartido = elPartido["nombrePartido"]
      partidoActual.lemaPartido = elPartido["lemaPartido"]
      return self.partidoRepositorio.save(partidoActual)
     
     def eliminarPartido(self,id):
        return self.partidoRepositorio.delete(id)
  
     def asignarPartidoCandidato(self,idCandidato,idPartido):
      candidatoActual = CandidatoModelo(self.candidatoRepositorio.findById(idCandidato))
      partidoActual=PartidoModelo(self.partidoRepositorio.findById(idPartido))
      candidatoActual.idPartido=partidoActual
      return self.candidatoRepositorio.save(candidatoActual)


