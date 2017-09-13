#ILYA CHABAN
import argparse


_draw_methods = {}
_parse_options = []
draw_parser = argparse.ArgumentParser(description="Draw parser")
draw_parser.add_argument('--text', type=str)
draw_parser.add_argument('--method', type=str, choices=_parse_options)


def parametrized(dec):
    """Transforms decorator into parametrized decorator"""
    def called_with_params(*args, **kwargs):
        def called_with_function(f):
            return dec(f, *args, **kwargs)
        return called_with_function
    return called_with_params

@parametrized
def draw_option(func, draw_method: str):
    """Registers draw function as draw_method in parser and drawer"""
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    _draw_methods[draw_method] = wrapper
    _parse_options.append(draw_method)
    return wrapper

def draw(data: dict, method: str) -> None:
    """Visualizes data in dict data using chosen in str draw method."""
    if method in _draw_methods:
        _draw_methods[method](data)