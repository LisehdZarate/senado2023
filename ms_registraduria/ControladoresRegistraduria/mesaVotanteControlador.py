from Repositorios.mesaVotanteRepositorio import MesaVotanteRepositorio
from ModelosRegistraduria.mesaVotanteModelo import MesaVotanteModelo

class MesaVotanteControlador():
         
     def __init__(self):
        self.mesaVotanteRepositorio = MesaVotanteRepositorio()
     
     def listarMesaVotante(self):
        return self.mesaVotanteRepositorio.findAll()

     def crearMesaVotante(self,laMesaVotante):
        nuevaMesaVotante=MesaVotanteModelo(laMesaVotante)
        return self.mesaVotanteRepositorio.save(nuevaMesaVotante)

     def mostrarMesaVotante(self,id):
      laMesaVotante=MesaVotanteModelo(self.mesaVotanteRepositorio.findById(id))
      return laMesaVotante.__dict__

     def actualizarMesaVotante(self,id,laMesaVotante):
      mesaVotanteActual=MesaVotanteModelo(self.mesaVotanteRepositorio.findById(id))
      mesaVotanteActual.numeroMesa=laMesaVotante["numeroMesa"]
      mesaVotanteActual.cedulaInscripta = laMesaVotante["cedulaInscripta"]
      return self.mesaVotanteRepositorio.save(mesaVotanteActual)
     
     def eliminarMesaVotante(self,id):
        return self.mesaVotanteRepositorio.delete(id)