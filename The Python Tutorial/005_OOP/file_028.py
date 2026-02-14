# Zero-argument form
# super().method(args…)
# Only valid inside a method defined in a class body.
# Python implicitly knows:
# - Which class you’re in (the one whose method you wrote).
# - Which instance or class was bound to self (or cls) in that method.
# It’s equivalent to super(CurrentClass, self).method(args…), but you don’t
# have to repeat the class name or self.


# Explicit form
# super(ThisClass, instance_of_cls)
# Useful in more dynamic contexts (e.g. in a function outside the class, or in a metaclass).


class A:
    def greet(self):
        print("Hello from A")


class B(A):
    def greet(self):
        print("Hello from B")


def call_parent_greet(obj):
    if isinstance(obj, B):
        # Explicitly call A's greet using super
        super(B, obj).greet()
    else:
        print("Invalid argument provided")


b = B()
b.greet()  # Output: Hello from B
call_parent_greet(b)  # Output: Hello from A
