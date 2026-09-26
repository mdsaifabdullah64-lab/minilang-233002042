class RuntimeError(Exception):
    pass


class StackMachine:
    def __init__(self):
        self.stack = []
        self.memory = {}
        self.pc = 0

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.stack:
            raise RuntimeError("Stack underflow")
        return self.stack.pop()

    def run(self, instructions):
        self.pc = 0

        while self.pc < len(instructions):
            instruction = instructions[self.pc]

            parts = instruction.strip().split()

            if not parts:
                self.pc += 1
                continue

            opcode = parts[0]

            if opcode == "PUSH":
                value = parts[1]

                if "." in value:
                    value = float(value)
                else:
                    value = int(value)

                self.push(value)

            elif opcode == "LOAD":
                name = parts[1]

                if name not in self.memory:
                    raise RuntimeError(
                        f"Undefined variable: {name}"
                    )

                self.push(self.memory[name])

            elif opcode == "STORE":
                name = parts[1]
                value = self.pop()
                self.memory[name] = value

            elif opcode == "ADD":
                b = self.pop()
                a = self.pop()
                self.push(a + b)

            elif opcode == "SUB":
                b = self.pop()
                a = self.pop()
                self.push(a - b)

            elif opcode == "MUL":
                b = self.pop()
                a = self.pop()
                self.push(a * b)

            elif opcode == "DIV":
                b = self.pop()
                a = self.pop()

                if b == 0:
                    raise RuntimeError(
                        "Division by zero"
                    )

                self.push(a / b)

            elif opcode == "PRINT":
                value = self.pop()
                print(value)

            elif opcode == "HALT":
                break

            else:
                raise RuntimeError(
                    f"Unknown instruction: {opcode}"
                )

            self.pc += 1

        return self.memory
