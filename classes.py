Introduction to Classes
In Python, a class is defined as follows:

 class Vehicle: # definition of the class Vehicle
    def __init__ (self, a, b = None):
        self.seats = a                      # number of seats in the vehicle
        self.passengers = b if b else []    # list containing passenger names

    def print_passengers (self):
        for i in range (len (self.passengers)):
            print (self.passengers [i])
            ```
``` py
car1 = Vehicle(4, ['Pierre', 'Adrian']) # instantiation of an object from the Vehicle class


===========================================
Based on syntax from the Vehicle class defined above:

(a) Define a new Complex class with 2 attributes:
part_re which contains the real part of a complex number.
part_im which contains the imaginary part of a complex number.
(b) Define in the Complex class adisplay method which prints a Complex in its algebraic form a ± bi. This method should adapt to the sign of the imaginary part (The method should be able to display 4 - 2i,6 + 2i, 5, ...).
(c) Instantiate two Complex objects corresponding to the complex numbers  4+5𝑖
  and  3−2𝑖
 , then print them on the console.


(d) Define in the Complex class an add method which takes as argument a Complex object and adds it to the instance calling the method. The result of this sum will be stored in the attributes of the Complex calling the method.
(e) Test the new add method on two instances of the Complex class and display their sum.


class Complex:
    def __init__(self, a, b):
        self.part_re = a
        self.part_im = b
        
    def display(self):
        if(self.part_im < 0):
            print(self.part_re,'-', -self.part_im,'i')
        if(self.part_im == 0):
            print(self.part_re)
        if(self.part_im > 0):
            print(self.part_re, '+',self.part_im,'i')
            
    def add(self, C):
        self.part_re = self.part_re + C.part_re
        self.part_im = self.part_im + C.part_im
        
C1 = Complex(4, -1)
C2 = Complex(-1, 3)

C1.add(C2)
C1.display()