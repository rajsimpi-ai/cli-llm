import sys
import argparse
from .cli import run_cli

def main():
    parser = argparse.ArgumentParser(
        prog="vak",
        description="VakSh ⚡ — Speech to Shell, Words to Power"
    )

    parser.add_argument(
        "prompt",
        nargs="*",
        help="Instruction or expression to process, e.g. vak \"2+2\""
    )

    args = parser.parse_args()

    if not args.prompt:
        parser.print_help()
        sys.exit(1)

    user_prompt = " ".join(args.prompt)
    run_cli(user_prompt)
