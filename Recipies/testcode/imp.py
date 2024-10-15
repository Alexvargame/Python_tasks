import importlib
import urllib.request
import sys
print(dir(importlib))
def load_module(url):
    u = urllib.request.urlopen(url)
    source = u.read().decode('utf-8')
    mod = sys.modules.setdefault(url, importlib.util.module_from_spec(1))
    code = compile(source, url, 'exec')
    mod.__file__ = url
    mod.__package__ = ''
    exec(code, mod.__dict__)
    return mod

fib = load_module('http://localhost:15000/fib.py')
