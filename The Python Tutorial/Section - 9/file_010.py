# Every Python object has a __class__ attribute pointing to its type.

class MyClass:
    def sayHello(self):
        print("Hello World!")


c = MyClass()

print(type(c))  # <class '__main__.MyClass'>
print(c.__class__)  # <class '__main__.MyClass'>
print(repr(MyClass))  # <class '__main__.MyClass'>

x = 3
print(type(x))  # <class 'int'>
print(x.__class__)  # <class 'int'>
print(repr(int))  # <class 'int'>
# The repr method in Python returns a string that represents the “official” 
# representation of an object.

s = "hello"
print(type(s))  # <class 'str'>
print(s.__class__)  # <class 'str'>
print(repr(str))  # <class 'str'>

print(repr(s))  # Hello
print(repr(x))  # 3
print(repr(c))  # <__main__.MyClass object at 0x102541be0>
print(repr(MyClass.sayHello)) # <function MyClass.sayHello at 0x1030f84a0>
print(repr(c.sayHello)) # <bound method MyClass.sayHello of <__main__.MyClass object at 0x10516dbe0>>
print(type(c.__class__))  # <class 'type'>


