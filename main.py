import sys

from lexer import Lexer
from parser import Parser
from semantic import SemanticAnalyzer
from tac import TACGenerator
from optimizer import Optimizer
from backend import StackBackend
from runtime import StackMachine


def main():

    if len(sys.argv) != 2:
        print(
            "Usage: python src/main.py <source-file>"
        )
        return

    filename = sys.argv[1]

    with open(filename, "r", encoding="utf-8") as file:
        source = file.read()

    print("========== SOURCE ==========")
    print(source)

    # 1. Lexer
    print("\n========== LEXER ==========")

    lexer = Lexer(source)
    tokens = lexer.tokenize()

    for token in tokens:
        print(token)

    # 2. Parser
    print("\n========== PARSER ==========")

    parser = Parser(tokens)
    ast = parser.parse()

    print("Parsing completed successfully.")

    # 3. Semantic Analysis
    print("\n========== SEMANTIC ANALYSIS ==========")

    analyzer = SemanticAnalyzer()
    analyzer.analyze(ast)

    if analyzer.errors:
        print("Semantic errors found:")

        for error in analyzer.errors:
            print(error)

        return

    print("Semantic analysis completed successfully.")

    # 4. TAC
    print("\n========== TAC ==========")

    tac_generator = TACGenerator()
    tac_code = tac_generator.generate(ast)

    for instruction in tac_code:
        print(instruction)

    # 5. Optimization
    print("\n========== OPTIMIZED TAC ==========")

    optimizer = Optimizer()

    optimized_code = optimizer.optimize(tac_code)

    for instruction in optimized_code:
        print(instruction)

    # 6. Backend
    print("\n========== STACK CODE ==========")

    backend = StackBackend()
    stack_code = backend.generate(optimized_code)

    for instruction in stack_code:
        print(instruction)

    # 7. Runtime
    print("\n========== EXECUTION ==========")

    runtime = StackMachine()
    memory = runtime.run(stack_code)

    print("\nFinal memory:")
    print(memory)


if __name__ == "__main__":
    main()
