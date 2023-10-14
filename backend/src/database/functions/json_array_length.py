from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import FunctionElement


__all__ = ("json_array_length", "compile")

class json_array_length(FunctionElement):
    name = 'json_array_len'
    inherit_cache = True


@compiles(json_array_length)
def compile(element, compiler, **_):
    return f"json_array_length({compiler.process(element.clauses)})"
