from Repositorios.resultadoRepositorio import ResultadoRepositorio
from ModelosRegistraduria.resultadoModelo import ResultadoModelo

class ResultadoControlador():
    
     def __init__(self):
        self.resultadoRepositorio = ResultadoRepositorio()
     
     def listarResultado(self):
        return self.resultadoRepositorio.findAll()

     def crearResultado(self,elResultado):
        nuevoResultado=ResultadoModelo(elResultado)
        return self.resultadoRepositorio.save(nuevoResultado)

     def mostrarResultado(self,id):
      elResultado=ResultadoModelo(self.resultadoRepositorio.findById(id))
      return elResultado.__dict__

     def actualizarResultado(self,id,elResultado):
      resultadoActual=ResultadoModelo(self.resultadoRepositorio.findById(id))
      resultadoActual.idResultado=elResultado["idResultado"]
      resultadoActual.numeroMesa = elResultado["numeroMesa"]
      resultadoActual.idCandidato = elResultado["idCandidato"]
      return self.resultadoRepositorio.save(resultadoActual)

     def eliminarResultado(self,id):
        return self.resultadoRepositorio.delete(id)