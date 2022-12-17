class ComplexNumber():
    
    def __init__(self, real, img):
        self.real = real
        self.img = img
        
    
    def __abs__(self):
        return (self.real ** 2 + self.img ** 2) ** (1/2)
    
        
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.img + other.img)
    
    
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.img - other.img)
    
    
    def __mul__(self, other):
        real_part = self.real * other.real - self.img * other.img
        img_part = self.img * other.real + self.real * other.img
        return ComplexNumber(real_part, img_part)
    
    
    def __eq__(self, other):
        return (self.real == other.real and self.img == other.img)
    
    
    def __str__(self):
        if self.real != 0:
            if self.img != 0:
                return str(self.real) + " + i" + str(self.img)
            else:
                return str(self.real)
        else:
            if self.img != 0:
                return "i" + str(self.img)
            else:
                return 0
