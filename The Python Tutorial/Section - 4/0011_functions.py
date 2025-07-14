# The keyword def introduces a function definition. It must be followed by the 
# function name and the parenthesized list of formal parameters. The statements 
# that form the body of the function start at the next line, and must be indented.
# The first statement of the function body can optionally be a string literal; 
# this string literal is the function’s documentation string, or docstring. 

def greet(name):
    """Greet a person by name."""
    print(f"Hello, {name}!")

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def factorial(n):
    """Return the factorial of a non-negative integer n."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# The execution of a function introduces a new symbol table used for the 
# local variables of the function. More precisely, all variable assignments 
# in a function store the value in the local symbol table; whereas variable 
# references first look in the local symbol table, then in the local symbol tables 
# of enclosing functions, then in the global symbol table, and finally in the table 
# of built-in names. Thus, global variables and variables of enclosing functions cannot be 
# directly assigned a value within a function (unless, for global variables, 
# named in a global statement, or, for variables of enclosing functions, 
# named in a nonlocal statement), although they may be referenced.

x = "global x"
y = "global y"

def outer():
    x = "outer x"
    y = "outer y"
    def inner():
        nonlocal x
        x = "inner x"
        print("inner:", x)
        y = "inner y"
        print("inner:", y)
    inner()
    print("outer:", x)
    print("outer:", y)

def change_global():
    global x
    x = "changed global x"
    y = "changed global y"

outer()
print("global before change_global:", x, y)
change_global()
print("global after change_global:", x, y)
"""
Output:

inner: inner x
inner: inner y
outer: inner x
outer: outer y

global before change_global: global x global y
global after change_global: changed global x global y
"""

# The arguments to a function call are introduced in the local symbol table of the called function 
# when it is called; thus, arguments are passed using call by value (where the value is always an object reference, 
# not the value of the object). When a function calls another function, or calls itself recursively, a new local symbol 
# table is created for that call.
def foo(a):
    print("foo's a:", a)
    a = 10
    print("foo's a after assignment:", a)

b = 5
print("global b before foo:", b)
foo(b)
print("global b after foo:", b)

def bar(lst):
    print("bar's lst:", lst)
    lst.append(4)
    print("bar's lst after append:", lst)

my_list = [1, 2, 3]
print("global my_list before bar:", my_list)
bar(my_list)
print("global my_list after bar:", my_list)

"""
Output:

global b before foo: 5
foo's a: 5
foo's a after assignment: 10
global b after foo: 5

global my_list before bar: [1, 2, 3]
bar's lst: [1, 2, 3]
bar's lst after append: [1, 2, 3, 4]
global my_list after bar: [1, 2, 3, 4]
"""

