import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.scanner import Scanner

class NeemeScript:
    @staticmethod
    def main():
        args = sys.argv[1:]
        if len(args) > 1:
            print("Usage: python3 src/interpreter.py [script_path]")
            sys.exit(64)
        elif len(args) == 1:
            NeemeScript.run_file(args[0])
        else:
            NeemeScript.run_prompt()

    @staticmethod
    def run_file(path: str):
        if not os.path.exists(path):
            print(f"Error: Source file '{path}' not found.")
            sys.exit(74)
        with open(path, "r", encoding="utf-8") as f:
            source = f.read()
        NeemeScript.run(source)

    @staticmethod
    def run_prompt():
        print("NeemeScript Interactive Mode (Type 'exit' to quit)")
        while True:
            try:
                line = input("neemescript> ")
                if line.strip() == "exit":
                    break
                if not line.strip():
                    continue
                NeemeScript.run(line)
            except (KeyboardInterrupt, EOFError):
                print("\nExiting...")
                break

    @staticmethod
    def run(source: str):
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()
        print("--- Scanned Tokens ---")
        for token in tokens:
            print(token)
        if scanner.has_error:
            print("Scan completed with errors.")

if __name__ == "__main__":
    NeemeScript.main()

