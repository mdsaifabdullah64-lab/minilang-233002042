class Optimizer:

    def constant_folding(self, code):
        optimized = []

        for instruction in code:
            # constant expression detect করে simplify করবে
            optimized.append(instruction)

        return optimized

    def dead_code_elimination(self, code):
        # unused assignments remove করবে
        return code

    def optimize(self, code):
        code = self.constant_folding(code)
        code = self.dead_code_elimination(code)

        return code
