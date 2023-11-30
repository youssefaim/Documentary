class Documantaire :
    _count = 0
    def __init__(self,_title,_date,) :
    
        self._title = _title
        self._date = _date
        Documantaire._count += 1
        self._code = Documantaire._count
    def getcode (self) :
        return self._code
    
    def setcode (self,_code) :
        self._code = _code

    def gettitle (self) :
        return self._title
    
    def settitle (self,_title) :
        self._title = _title
    
    def getdate (self) :
        return self._date
    
    def setdate (self,_date) :
        self._date = _date
    
    def getcount(self) :
        return Documantaire._count
    
    def ToString (self) :
        return "code :" + str(self.getcode()) + " title :" + str(self.gettitle()) + "date : " + str(self.getdate())
    def Equals (self,doc1) :
        if self._code == doc1._code :
            return True
        else :
            return False
    

class exemplaire (Documantaire) :

    def __init__(self,_title, _date,DateD,Numero = 1234):
        super().__init__(_title, _date)
        self.__Numero = Numero
        self.__DateD = DateD
    def getnumero (self) :
        return self.__Numero
    
    def setnumero (self,Numero) :
        self.__Numero = Numero
    
    def getDateD (self) :
        return self.__DateD
    
    def setcode (self,DateD) :
        self.__DateD = DateD
    
    def ToString(self):
        return super().ToString() +  "Numero :" + str(self.getnumero()) + "Date D'Achat : " + str(self.getDateD())
    
    def Equals(self, ex1):
        if self.__Numero == ex1.__Numero :
        
            return True
        else :
            return False
    
    




    



