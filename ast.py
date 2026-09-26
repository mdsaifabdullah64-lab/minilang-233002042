from dataclasses import dataclass


@dataclass
class StructField:
    name: str
    field_type: str


@dataclass
class StructDecl:
    name: str
    fields: list
