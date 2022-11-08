from Repositorios.partidoRepositorio import PartidoRepositorio
from ModelosRegistraduria.partidoModelo import PartidoModelo

class PartidoControlador():
    
     def __init__(self):
        self.partidoRepositorio = PartidoRepositorio()
     
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
  
