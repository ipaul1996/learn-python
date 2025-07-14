class LoggerMixin:
    def log(self):
        print("Log")


class AuthMixin:
    def auth(self):
        print("Auth")


class BaseResource:
    def get(self):
        print("Get")


class MyResource(LoggerMixin, AuthMixin, BaseResource):
    pass


print(MyResource.__mro__)
# (<class '__main__.MyResource'>, <class '__main__.LoggerMixin'>, <class '__main__.AuthMixin'>, <class '__main__.BaseResource'>, <class 'object'>)


