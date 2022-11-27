from Repositorios.resultadoRepositorio import ResultadoRepositorio
from Repositorios.mesaVotanteRepositorio import MesaVotanteRepositorio
from Repositorios.candidatoRepositorio import CandidatoRepositorio
from ModelosRegistraduria.resultados import Resultados
from ModelosRegistraduria.mesaVotanteModelo import MesaVotanteModelo
from ModelosRegistraduria.candidatoModelo import CandidatoModelo

class ResultadoControlador():
    
     def __init__(self):
        self.resultadoRepositorio = ResultadoRepositorio()
        self.mesaRepositorio = MesaVotanteRepositorio()
        self.candidatoRepositorio = CandidatoRepositorio()
     
     def listarResultado(self):
        return self.resultadoRepositorio.findAll()

     def crearResultado(self,elResultado):
        nuevoResultado=Resultados(elResultado)
        return self.resultadoRepositorio.save(nuevoResultado)

     def mostrarResultado(self,id):
      elResultado=Resultados(self.resultadoRepositorio.findById(id))
      return elResultado.__dict__

     def actualizarResultado(self,id,elResultado):
      resultadoActual=Resultados(self.resultadoRepositorio.findById(id))
      resultadoActual.idResultado=elResultado["idResultado"]
      resultadoActual.numeroMesa = elResultado["numeroMesa"]
      resultadoActual.idCandidato = elResultado["idCandidato"]
      resultadoActual.numerovotos = elResultado["numerovotos"]
      return self.resultadoRepositorio.save(resultadoActual)

     def eliminarResultado(self,id):
        return self.resultadoRepositorio.delete(id)
     
     def asignarMesaResultado(self,idMesaVotante,idResultado):
      mesaVotanteActual = MesaVotanteModelo(self.mesaVotanteRepositorio.findById(idMesaVotante))
      resultadoActual=Resultados(self.resultadoRepositorio.findById(idResultado))
      mesaVotanteActual.idResultado=resultadoActual
      return self.mesaVotanteRepositorio.save(mesaVotanteActual)

     def asignarCandidatoResultado(self,idCandidato,idResultado):
      CandidatoActual = CandidatoModelo(self.candidatoRepositorio.findById(idCandidato))
      resultadoActual=Resultados(self.resultadoRepositorio.findById(idResultado))
      CandidatoActual.idResultado=resultadoActual
      return self.candidatoRepositorio.save(CandidatoActual)
      
     def SumaVotosCandidato(self):
      return self.resultadoRepositorio.getSumaVotosCandidato() 
     def SumaVotosMesa(self):
      return self.resultadoRepositorio.getSumaVotosMesa() 
     def SumaVotosPartido(self):
      return self.resultadoRepositorio.getSumaVotosPartido()
     def SumaVotosPorcentaje(self):
      return self.resultadoRepositorio.getSumaVotosPorcentaje()
     def SumaVotosMesaEsp(self,idMesa):
      return self.resultadoRepositorio.getSumaVotosMesaEsp(idMesa)

