from dataclasses import dataclass


@dataclass
class Program:
    declarations: list


@dataclass
class StructDecl:
    name: str
    fields: list


@dataclass
class FunctionDecl:
    name: str
    params: list
    body: object
    return_type: str


@dataclass
class VariableDecl:
    name: str
    var_type: str
    initializer: object = None


@dataclass
class Block:
    statements: list


@dataclass
class Assignment:
    name: str
    value: object


@dataclass
class BinaryOp:
    left: object
    operator: str
    right: object


@dataclass
class Literal:
    value: object


@dataclass
class Variable:
    name: str


@dataclass
class Return:
    value: object
