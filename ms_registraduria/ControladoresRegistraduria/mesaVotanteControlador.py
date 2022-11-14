from Repositorios.mesaVotanteRepositorio import MesaVotanteRepositorio
from Repositorios.mesaRepositorio import MesaRepositorio
from ModelosRegistraduria.mesaVotanteModelo import MesaVotanteModelo
from ModelosRegistraduria.mesaModelo import MesaModelo

class MesaVotanteControlador():
         
     def __init__(self):
        self.mesaVotanteRepositorio = MesaVotanteRepositorio()
        self.mesaRepositorio = MesaRepositorio()

     
     def listarMesaVotante(self):
        return self.mesaVotanteRepositorio.findAll()

     def crearMesaVotante(self,laMesaVotante, laMesa):
        nuevaMesaVotante=MesaVotanteModelo(laMesaVotante)
        laMesa=MesaModelo(self.mesaRepositorio.findById(laMesa))
        nuevaMesaVotante.Mesa=laMesa
        return self.mesaVotanteRepositorio.save(nuevaMesaVotante)

     def mostrarMesaVotante(self,id):
      laMesaVotante=MesaVotanteModelo(self.mesaVotanteRepositorio.findById(id))
      return laMesaVotante.__dict__

     def actualizarMesaVotante(self,id,laMesaVotante, idMesa):
      mesaVotanteActual=MesaVotanteModelo(self.mesaVotanteRepositorio.findById(id))
      mesaVotanteActual.cedulaInscripta = laMesaVotante["cedulaInscripta"]
      laMesa=MesaModelo(self.mesaRepositorio.findById(idMesa))
      mesaVotanteActual.laMesa= laMesa
      return self.mesaVotanteRepositorio.save(mesaVotanteActual)
     
     def eliminarMesaVotante(self,id):
        return self.mesaVotanteRepositorio.delete(id)

