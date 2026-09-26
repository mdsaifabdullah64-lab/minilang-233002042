class TACGenerator:

    def __init__(self):
        self.code = []
        self.temp_count = 0

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def emit(self, instruction):
        self.code.append(instruction)

    def generate_binary(self, left, op, right):
        temp = self.new_temp()

        self.emit(
            f"{temp} = {left} {op} {right}"
        )

        return temp
