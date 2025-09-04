from .llm_providers import simple_calculator

def run_cli(prompt: str):
    result = simple_calculator(prompt)

    expression, value = result.split("=")
    expression = expression.strip()
    value = value.strip()

    print(f"\n{expression} : \"{value}\"")

    choice = input().strip().lower()

    if choice == "":
        print(f"{value}")
    elif choice == "e":
        new_prompt = input("✏️ Enter new prompt: ")
        run_cli(new_prompt)
    else:
        print("Cancelled.")