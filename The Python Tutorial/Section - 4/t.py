class Base:
    def greet(self):
        self.say_hello()

    def say_hello(self):
        print("Hello from Base")


class A:
    def greet(self):
        print("Hello from A")


class B(A):
    def greet(self):
        print(super())
        super().greet()  # find next greet() in MRO (A)
        print("…and hello from B")


b = B()
b.greet()
# Hello from A
# …and hello from B
