from __future__ import annotations
from televisores.marca import Marca
class TV:
    _numTV=0
    def __init__(self,marca,estado):
         self._marca=marca
         self._estado=estado
         self._canal=1
         self._volumen=1
         self._precio=500
         self._control=None
         TV._numTV+=1
         
    def setMarca(self,mar):
        self._marca=mar
    def getMarca(self):
        return self._marca
    
    def setCanal(self,can):
        if can>=1 and can<=120 and self._estado==True:
            self._canal=can
    def getCanal(self):
        return self._canal
    
    def setPrecio(self,pre):
        self._precio=pre
    def getPrecio(self):
        return self._precio
    
    def setVolumen(self,vol):
        if vol>=1 and vol<=7 and self._estado==True:
            self._volumen=vol
    def getVolumen(self):
        return self._volumen
    
    def setControl(self,con):
        self._control=con
    def getControl(self):
        return self._control
    
    @classmethod
    def setNumTV(cls,n):
        cls._numTV=n
    def getNumTV(cls):
        return cls._numTV
    
    def turnOn(self):
        self._estado=True
    def turnOff(self):
        self._estado=False
        
    def canalUp(self):
        if self._canal>=1 and self._canal<120 and self._estado==True:
            self._canal+=1
    def canalDown(self):
        if self._canal>1 and self._canal<=120 and self._estado==True:
            self._canal-=1
            
    def volumenUp(self):
        if self._volumen>=0 and self._volumen<7 and self._estado==True:
            self._volumen+=1
    def volumenDown(self):
        if self._volumen>0 and self._volumen<=7 and self._estado==True:
            self._volumen-=1

    def getEstado(self):
        return self._estado
         
        
        