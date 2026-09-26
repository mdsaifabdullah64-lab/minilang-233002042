class Optimizer:

    def constant_folding(self, code):
        optimized = []

        for instruction in code:

            parts = instruction.split()

            # Example:
            # t1 = 10 + 20

            if len(parts) == 5 and parts[1] == "=":

                target = parts[0]
                left = parts[2]
                operator = parts[3]
                right = parts[4]

                try:
                    a = float(left)
                    b = float(right)

                    if operator == "+":
                        result = a + b

                    elif operator == "-":
                        result = a - b

                    elif operator == "*":
                        result = a * b

                    elif operator == "/":
                        if b == 0:
                            optimized.append(instruction)
                            continue

                        result = a / b

                    else:
                        optimized.append(instruction)
                        continue

                    if result.is_integer():
                        result = int(result)

                    optimized.append(
                        f"{target} = {result}"
                    )

                except ValueError:
                    optimized.append(instruction)

            else:
                optimized.append(instruction)

        return optimized


    def dead_code_elimination(self, code):

        used_variables = set()

        # Find variables that are used
        for instruction in code:

            parts = instruction.split()

            if len(parts) >= 3:

                for part in parts[2:]:
                    if part.isidentifier():
                        used_variables.add(part)

        optimized = []

        for instruction in code:

            parts = instruction.split()

            # Example:
            # x = 10

            if len(parts) == 3 and parts[1] == "=":

                variable = parts[0]

                if variable not in used_variables:
                    continue

            optimized.append(instruction)

        return optimized


    def optimize(self, code):

        code = self.constant_folding(code)

        code = self.dead_code_elimination(code)

        return code
