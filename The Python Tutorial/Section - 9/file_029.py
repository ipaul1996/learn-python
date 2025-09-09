class Model:
    def save(self):
        print("Saving to DB")


class LoggingMixin:
    def save(self):
        print("Logging")


class ValidationMixin(LoggingMixin):
    def save(self):
        print("Validating")
        super().save()


class MyModel(ValidationMixin, LoggingMixin, Model):
    pass


obj = MyModel()
obj.save()
# MRO: [MyModel, ValidationMixin, LoggingMixin, Model, object]
# Output:
# Validating
# Logging
# Saving to DB
