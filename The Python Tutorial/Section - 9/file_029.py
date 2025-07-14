class LoggingMixin:
    def save(self):
        print("Logging")
        super().save()


class ValidationMixin:
    def save(self):
        print("Validating")
        super().save()


class Model:
    def save(self):
        print("Saving to DB")


class MyModel(LoggingMixin, ValidationMixin, Model):
    pass


obj = MyModel()
obj.save()
# MRO: [MyModel, LoggingMixin, ValidationMixin, Model, object]
# LoggingMixin.save
# ValidationMixin.save
# Model.save
