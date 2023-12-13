from abc import ABC as abstractionmethod

class shape:

    @abstractionmethod
    def area():
        pass

    @abstractionmethod
    def perimeter():
        pass

    @abstractionmethod
    def numb_of_side():
        pass

    @abstractionmethod
    def __str__():
        pass

    @abstractionmethod
    def __eq__():
        pass
    

class Triangle(shape):

    def __int__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        return self.a + self.b + self.c

    def perimeter(self):
        x = area() / 2
        return  (x * (x - self.a) * (x - self.b)* (x - self.c)) * 0.5

    def numb_of_side(self):
        return 3

    def __str__(self):
        return f'Trinangle with {self.a}, {self.b}, {self.c}'

        