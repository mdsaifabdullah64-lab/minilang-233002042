class Symbol:
    def __init__(self, name, symbol_type, kind):
        self.name = name
        self.symbol_type = symbol_type
        self.kind = kind


class Scope:
    def __init__(self, parent=None):
        self.parent = parent
        self.symbols = {}

    def define(self, symbol):
        if symbol.name in self.symbols:
            raise Exception(
                f"Duplicate declaration: {symbol.name}"
            )

        self.symbols[symbol.name] = symbol

    def lookup(self, name):
        if name in self.symbols:
            return self.symbols[name]

        if self.parent:
            return self.parent.lookup(name)

        return None


class SymbolTable:
    def __init__(self):
        self.current_scope = Scope()

    def enter_scope(self):
        self.current_scope = Scope(self.current_scope)

    def exit_scope(self):
        if self.current_scope.parent:
            self.current_scope = self.current_scope.parent

    def define(self, symbol):
        self.current_scope.define(symbol)

    def lookup(self, name):
        return self.current_scope.lookup(name)
