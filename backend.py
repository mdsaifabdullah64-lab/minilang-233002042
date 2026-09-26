class StackBackend:

    def generate(self, tac_code):
        output = []

        for instruction in tac_code:
            instruction = instruction.strip()

            if not instruction:
                continue

            # Binary operation
            parts = instruction.split()

            if len(parts) == 5 and parts[1] == "=":
                target = parts[0]
                left = parts[2]
                operator = parts[3]
                right = parts[4]

                self.emit_load(output, left)
                self.emit_load(output, right)

                if operator == "+":
                    output.append("ADD")

                elif operator == "-":
                    output.append("SUB")

                elif operator == "*":
                    output.append("MUL")

                elif operator == "/":
                    output.append("DIV")

                else:
                    raise ValueError(
                        f"Unsupported operator: {operator}"
                    )

                output.append(f"STORE {target}")

            # Simple assignment
            elif len(parts) == 3 and parts[1] == "=":
                target = parts[0]
                value = parts[2]

                self.emit_load(output, value)
                output.append(f"STORE {target}")

        output.append("HALT")

        return output

    def emit_load(self, output, value):

        try:
            if "." in value:
                float(value)
                output.append(f"PUSH {value}")
                return

            int(value)
            output.append(f"PUSH {value}")
            return

        except ValueError:
            pass

        output.append(f"LOAD {value}")
