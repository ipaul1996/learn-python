# super()
# The super() function returns a special object that allows you to call methods
# from a parent or superclass without explicitly naming it. When you use super() in a method,
# it finds and calls the next method with the same name in the method resolution order (MRO).
# This is especially useful in inheritance hierarchies (including multiple inheritance),
# as it makes your code more flexible and maintainable by avoiding hard-coded class names.
# In summary, super() helps you delegate method calls up the inheritance chain in a clean way.


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
# <super: <class 'B'>, <B object>>
# Hello from A
# …and hello from B




# Multiple Inheritance with super()
# Simulating a user notification system
class BaseNotifier:
    def notify(self, message):
        print(f"Logging notification: {message}")


class EmailNotifier(BaseNotifier):
    def notify(self, message):
        print("Preparing email...")
        super().notify(message)  # Delegates to BaseNotifier
        print(f"Sending email: {message}")


class SMSNotifier(BaseNotifier):
    def notify(self, message):
        print("Preparing SMS...")
        super().notify(message)  # Delegates to BaseNotifier
        print(f"Sending SMS: {message}")


class MultiChannelNotifier(EmailNotifier, SMSNotifier):
    def notify(self, message):
        print("Starting multi-channel notification")
        super().notify(message)  # Follows MRO: EmailNotifier -> SMSNotifier -> BaseNotifier
        print("Finished multi-channel notification")


notifier = MultiChannelNotifier()
notifier.notify("System maintenance at 2 AM")



