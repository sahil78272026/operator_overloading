# Operator Overloading
class Number:
    def __init__(self, num):  # init is a constructor and also know as dunder method
        self.num = num

    def __add__(self, num2): # predefinedd dunder methods
        print("Lets add")
        return self.num + num2.num

    def __mul__(self, num2): # predefinedd dunder methods
        print("Lets multiply")
        return self.num * num2.num

n1 = Number(4)
n2 = Number(6)
sum = n1 + n2
mul = n1 * n2
print(sum)
print(mul)