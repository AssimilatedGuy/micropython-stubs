from typing import Any

class ArithmeticError: ...
class AssertionError: ...
class AttributeError: ...
class BaseException: ...
class EOFError: ...
Ellipsis = Any

class Exception: ...
class GeneratorExit: ...
class ImportError: ...
class IndentationError: ...
class IndexError: ...
class KeyError: ...
class KeyboardInterrupt: ...
class LookupError: ...
class MemoryError: ...
class NameError: ...
NotImplemented = Any

class NotImplementedError: ...
class OSError: ...
class OverflowError: ...
class RuntimeError: ...
class StopAsyncIteration: ...
class StopIteration: ...
class SyntaxError: ...
class SystemExit: ...
class TypeError: ...
class UnicodeError: ...
class ValueError: ...
class ViperTypeError: ...
class ZeroDivisionError: ...

def abs() -> Any: ...
def all() -> Any: ...
def any() -> Any: ...
def bin() -> Any: ...

class bool: ...

class bytearray:
    def append(self) -> Any: ...
    def decode(self) -> Any: ...
    def extend(self) -> Any: ...

class bytes:
    def center(self) -> Any: ...
    def count(self) -> Any: ...
    def decode(self) -> Any: ...
    def endswith(self) -> Any: ...
    def find(self) -> Any: ...
    def format(self) -> Any: ...
    def index(self) -> Any: ...
    def isalpha(self) -> Any: ...
    def isdigit(self) -> Any: ...
    def islower(self) -> Any: ...
    def isspace(self) -> Any: ...
    def isupper(self) -> Any: ...
    def join(self) -> Any: ...
    def lower(self) -> Any: ...
    def lstrip(self) -> Any: ...
    def partition(self) -> Any: ...
    def replace(self) -> Any: ...
    def rfind(self) -> Any: ...
    def rindex(self) -> Any: ...
    def rpartition(self) -> Any: ...
    def rsplit(self) -> Any: ...
    def rstrip(self) -> Any: ...
    def split(self) -> Any: ...
    def splitlines(self) -> Any: ...
    def startswith(self) -> Any: ...
    def strip(self) -> Any: ...
    def upper(self) -> Any: ...

def callable() -> Any: ...
def chr() -> Any: ...

class classmethod: ...

def compile() -> Any: ...

class complex: ...

def delattr() -> Any: ...

class dict:
    def clear(self) -> Any: ...
    def copy(self) -> Any: ...
    def fromkeys(self) -> Any: ...
    def get(self) -> Any: ...
    def items(self) -> Any: ...
    def keys(self) -> Any: ...
    def pop(self) -> Any: ...
    def popitem(self) -> Any: ...
    def setdefault(self) -> Any: ...
    def update(self) -> Any: ...
    def values(self) -> Any: ...

def dir() -> Any: ...
def divmod() -> Any: ...

class enumerate: ...

def eval() -> Any: ...
def exec() -> Any: ...
def execfile() -> Any: ...

class filter: ...
class float: ...

class frozenset:
    def copy(self) -> Any: ...
    def difference(self) -> Any: ...
    def intersection(self) -> Any: ...
    def isdisjoint(self) -> Any: ...
    def issubset(self) -> Any: ...
    def issuperset(self) -> Any: ...
    def symmetric_difference(self) -> Any: ...
    def union(self) -> Any: ...

def getattr() -> Any: ...
def globals() -> Any: ...
def hasattr() -> Any: ...
def hash() -> Any: ...
def help() -> Any: ...
def hex() -> Any: ...
def id() -> Any: ...
def input() -> Any: ...

class int:
    def from_bytes(self) -> Any: ...
    def to_bytes(self) -> Any: ...

def isinstance() -> Any: ...
def issubclass() -> Any: ...
def iter() -> Any: ...
def len() -> Any: ...

class list:
    def append(self) -> Any: ...
    def clear(self) -> Any: ...
    def copy(self) -> Any: ...
    def count(self) -> Any: ...
    def extend(self) -> Any: ...
    def index(self) -> Any: ...
    def insert(self) -> Any: ...
    def pop(self) -> Any: ...
    def remove(self) -> Any: ...
    def reverse(self) -> Any: ...
    def sort(self) -> Any: ...

def locals() -> Any: ...

class map: ...

def max() -> Any: ...

class memoryview: ...

def min() -> Any: ...
def next() -> Any: ...

class object: ...

def oct() -> Any: ...
def open() -> Any: ...
def ord() -> Any: ...
def pow() -> Any: ...
def print() -> Any: ...

class property:
    def deleter(self) -> Any: ...
    def getter(self) -> Any: ...
    def setter(self) -> Any: ...

class range: ...

def repr() -> Any: ...

class reversed: ...

def round() -> Any: ...

class set:
    def add(self) -> Any: ...
    def clear(self) -> Any: ...
    def copy(self) -> Any: ...
    def difference(self) -> Any: ...
    def difference_update(self) -> Any: ...
    def discard(self) -> Any: ...
    def intersection(self) -> Any: ...
    def intersection_update(self) -> Any: ...
    def isdisjoint(self) -> Any: ...
    def issubset(self) -> Any: ...
    def issuperset(self) -> Any: ...
    def pop(self) -> Any: ...
    def remove(self) -> Any: ...
    def symmetric_difference(self) -> Any: ...
    def symmetric_difference_update(self) -> Any: ...
    def union(self) -> Any: ...
    def update(self) -> Any: ...

def setattr() -> Any: ...

class slice: ...

def sorted() -> Any: ...

class staticmethod: ...

class str:
    def center(self) -> Any: ...
    def count(self) -> Any: ...
    def encode(self) -> Any: ...
    def endswith(self) -> Any: ...
    def find(self) -> Any: ...
    def format(self) -> Any: ...
    def index(self) -> Any: ...
    def isalpha(self) -> Any: ...
    def isdigit(self) -> Any: ...
    def islower(self) -> Any: ...
    def isspace(self) -> Any: ...
    def isupper(self) -> Any: ...
    def join(self) -> Any: ...
    def lower(self) -> Any: ...
    def lstrip(self) -> Any: ...
    def partition(self) -> Any: ...
    def replace(self) -> Any: ...
    def rfind(self) -> Any: ...
    def rindex(self) -> Any: ...
    def rpartition(self) -> Any: ...
    def rsplit(self) -> Any: ...
    def rstrip(self) -> Any: ...
    def split(self) -> Any: ...
    def splitlines(self) -> Any: ...
    def startswith(self) -> Any: ...
    def strip(self) -> Any: ...
    def upper(self) -> Any: ...

def sum() -> Any: ...

class super: ...

class tuple:
    def count(self) -> Any: ...
    def index(self) -> Any: ...

class type: ...
class zip: ...
