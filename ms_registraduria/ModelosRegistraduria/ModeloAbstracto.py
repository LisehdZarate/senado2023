from abc import ABCMeta

class ModeloAbstracto(metaclass=ABCMeta):
    def __init__(self,data):
        for llave, valor in data.items():
            setattr(self, llave, valor)