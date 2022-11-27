from Repositorios.mesaRepositorio import MesaRepositorio
from ModelosRegistraduria.mesaModelo import MesaModelo

class MesaContralador():
     
     def __init__(self):
        self.mesaRepositorio = MesaRepositorio()
     
     def listarMesa(self):
        return self.mesaRepositorio.findAll()

     def crearMesa(self,laMesa):
      nuevaMesa=MesaModelo(laMesa)
      return self.mesaRepositorio.save(nuevaMesa)

     def mostrarMesa(self,id):
      laMesa=MesaModelo(self.mesaRepositorio.findById(id))
      return laMesa.__dict__

     def actualizarMesa(self,id,laMesa):
      mesaActual=MesaModelo(self.mesaRepositorio.findById(id))
      mesaActual.numeroMesa=laMesa["numeroMesa"]
      mesaActual.ubicacionMesa = laMesa["ubicacionMesa"]
      return self.mesaRepositorio.save(mesaActual)
     
     def eliminarMesa(self,id):
        return self.mesaRepositorio.delete(id)

