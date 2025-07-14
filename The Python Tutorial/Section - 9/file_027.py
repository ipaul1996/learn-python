# super()
# The super() function returns a special object called a "proxy object."
# This proxy object delegates method calls to a parent or superclass,
# allowing you to call methods from the next class in the method resolution order (MRO)
# after the current class. The proxy object doesn't represent the parent class itself,
# but acts as an intermediary that forwards your method calls appropriately.
# This is useful in inheritance, especially with multiple inheritance,
# because it helps you call parent class methods in a flexible and maintainable way,
# without hard-coding the parent class name.


class A:
    def greet(self):
        print("Hello from A")


class B(A):
    def greet(self):
        super().greet()  # find next greet() in MRO (A)
        print("…and hello from B")


b = B()
b.greet()
# Hello from A
# …and hello from B
