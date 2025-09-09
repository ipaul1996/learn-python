from pydantic import BaseModel
from pathlib import Path
from loguru import logger

class Foo(BaseModel):
    count: int
    size: float | None = None


class Bar(BaseModel):
    apple: str = "x"
    banana: str = "y"


class Spam(BaseModel):
    foo: Foo
    bars: list[Bar]


m = Spam(foo=Foo(count=1, size=3), bars=[Bar(), Bar(apple="u", banana="v")])

PROJECT_PATH = Path(__file__).absolute().parent
print(PROJECT_PATH)
