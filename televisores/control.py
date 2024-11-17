from __future__ import annotations
from televisores.tv import TV
class Control:
    def __init__(self):
        self._tv=None
        
    def enlazar(self,tv):
        self._tv=tv
        self._tv.setControl(self)
    def turnOn(self):
        self._tv.turnOn()
    def turnOff(self):
        self._tv.turnOff()
    def canalUp(self):
        self._tv.canalUp()
    def canalDown(self):
        self._tv.canalDown()
    def volumenUp(self):
        self._tv.volumenUp()
    def volumenDown(self):
        self._tv.volumenDown()
    def setCanal(self,c):
        self._tv.setCanal(c)
    def setVolumen(self,v):
        self._tv.setVolumen(v)
        
    def setTv(self,tv):
        self._tv=tv
    def getTv(self):
        return self._tv
    
        
    