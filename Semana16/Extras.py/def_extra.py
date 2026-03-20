class Operaciones:
    def __init__(self, num1, num2):
        self.number1 = num1
        self.number2 = num2

    def division(self): 
        if self.number2 == 0: 
            raise ValueError("No se puede dividir por cero")
        return self.number1 / self.number2  
    
    
    def multiplicacion(self):
        return self.number1 * self.number2 
    
    
    def promedio(self): 
        return (self.number1 + self.number2) / 2 

    
    def suma(self): 
        return self.number1 + self.number2 

    
    def conversion_grados_a_fahrenheid(self): 
        return (self.number1 * 9/5) + 32
      

         
