class SemanticError(Exception):
    pass


class SemanticAnalyzer:

    def __init__(self):
        self.errors = []

    def error(self, message, line=None, column=None):
        if line is not None:
            message = f"Line {line}, Column {column}: {message}"

        self.errors.append(message)

    def analyze(self, ast):
        # AST-এর semantic analysis শুরু হবে
        pass

    def check_variable_declaration(self, node):
        pass

    def check_assignment(self, node):
        pass

    def check_function(self, node):
        pass

    def check_struct(self, node):
        pass

    def check_expression(self, node):
        pass

    def check_return(self, node):
        pass
