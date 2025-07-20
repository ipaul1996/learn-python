from typing import final


@final
class BaseService:
    def serve(self) -> None:
        print("Service running")


# class MyService(BaseService): pass
# Base class "BaseService" is marked final and cannot be subclassed


class Handler:
    @final
    def handle(self) -> None:
        print("Handling")


"""
class CustomHandler(Handler):
    def handle(self) -> None:
        print("Oops")

Method "handle" cannot override final method defined in class "Handler"
"""

"""
@final on a class means “no subclasses allowed.”
@final on a method means “no overrides allowed.”
"""
